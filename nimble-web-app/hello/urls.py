from django.urls import include, path
from django.conf.urls import url
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('messages', views.get_messages)
]

urlpatterns += staticfiles_urlpatterns()