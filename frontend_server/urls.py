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

from handlers.main import handle_url as handle_main
from handlers.category import handle_url as handle_category
from handlers.article import handle_url as handle_article

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [ path('favicon.ico', favicon_view) ]

urls = []
current_path = []

urlpatterns.append(path('', handle_main))
urlpatterns.append(path('category/<str:category>', handle_category))
urlpatterns.append(path('article/<str:article_url>', handle_article))

urlpatterns.append(path('register/', handle_main, name='register'))
urlpatterns.append(path('login/', handle_main, name='login'))
urlpatterns.append(path('logout/', handle_main, name='logout'))
urlpatterns.append(path('editor/', handle_main, name='editor'))

print("urls:", urls)


