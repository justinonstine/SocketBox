from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from socketbox import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^socketbox/', include('socketbox.urls')),
    url(r'^accounts/register', views.register, name="register"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}), )