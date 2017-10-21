"""backend URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from rest_framework_jwt.views import obtain_jwt_token

from chat.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/', admin.site.urls),
    url(r'^auth', obtain_jwt_token),
    url(r'^profile/', include("profiles.urls", namespace='profiles')),
    url(r'^chat/', include("chat.urls", namespace='chat')),
]
