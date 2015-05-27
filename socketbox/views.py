from django.shortcuts import render
from socketbox.models import UserProfile, Location
from django.contrib.auth.models import User
from forms import UserForm, UserProfileForm, LocationForm


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
    else:
        profileForm = UserProfile()
        locationForm = Location()
        userForm = User()

    contextDict = {'profileForm': profileForm, 'locationForm': locationForm,
                   'userForm': userForm}

    return render(request, "registration/registration_form.html", contextDict)