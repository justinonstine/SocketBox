__author__ = 'justinonstine'
from django.conf.urls import patterns, url
from socketbox import views

urlpatterns = patterns("",
                       url(r'^$', views.index, name='index'),
                       url(r'^profile$', views.profile, name='profile'),
                       url(r'^accounts/register$', views.register, name='register'),
                       )