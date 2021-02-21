"""z_sort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from handlers import main_handler

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [ path('favicon.ico', favicon_view) ]

urls = []
current_path = []

urlpatterns.append(path('', main_handler.handle_url))

urlpatterns.append(path('register/', main_handler.handle_url, name='register'))
urlpatterns.append(path('login/', main_handler.handle_url, name='login'))
urlpatterns.append(path('logout/', main_handler.handle_url, name='logout'))
urlpatterns.append(path('editor/', main_handler.handle_url, name='editor'))

print("urls:", urls)


