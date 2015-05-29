from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from socketbox.models import UserProfile, Location, Tool
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from forms import UserForm, UserProfileForm, LocationForm
from django.db.models import Q
import re, json

def index(request):
    return render(request, 'socketbox/index.html', {})

def profile(request):
    return index(request)

def register(request):
    if request.method == 'POST':
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileForm(data=request.POST)
        locationForm = LocationForm(data=request.POST)

        if userForm.is_valid() and profileForm.is_valid() and \
           locationForm.is_valid():
            userObj = userForm.save()
            userObj.set_password(userObj.password)
            userObj.save()

            location = locationForm.save(commit=False)
            location.name = 'Home'
            location.save()

            profileObj = profileForm.save(commit=False)
            profileObj.user = userObj
            profileObj.address = location
            profileObj.save()
            profileObj.locations.add(location)
            profileObj.save()

            userObj = authenticate(username=userObj.username,
                                   password=userObj.password)
            login(request, userObj)

            return render(request, 'socketbox/index.html', {})
        else:
            if not locationForm.is_valid():
                print("Location is bad!")
                print locationForm.errors
            if not userForm.is_valid():
                print("user is bad!")
                print userForm.errors
                print request.POST
            if not profileForm.is_valid():
                print("profile is bad!")
                print profileForm.errors
            return index(request)
    else:
        profileForm = UserProfile()
        locationForm = Location()
        userForm = User()

    contextDict = {'profileForm': profileForm, 'locationForm': locationForm,
                   'userForm': userForm}

    return render(request, "registration/registration_form.html", contextDict)


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields.keys():
            qString = "%s__contains" % field_name
            if search_fields[field_name] != "":
                qString = "%s__%s__contains" % (field_name, search_fields[field_name])
            q = Q(**{qString: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query | or_query
    return query


def search(request):
    if request.method == 'POST':
        searchStr = request.POST['search']
        query = get_query(searchStr, {'description':"", 'name':"", 'size':"", \
                                      'category':"name"})
        if query:
            tools = Tool.objects.filter(query)
            return render(request, "socketbox/search_result.html", {"results":tools})
        else:
            return HttpResponse("<p>Could not understand query</p>")
    else:
        return render(request, "socketbox/search.html", {})
