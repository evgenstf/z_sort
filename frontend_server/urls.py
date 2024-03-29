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
from django.conf.urls import handler404, handler500

from handlers.main import handle_url as handle_main
from handlers.category import handle_url as handle_category
from handlers.article import handle_url as handle_article
from handlers.auth import handle_register
from handlers.auth import handle_login
from handlers.auth import handle_logout
from handlers.editor import handle_editor
from handlers.user_page import handle_user_page as handle_user
from handlers.error import handle_404, handle_500

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [ path('favicon.ico', favicon_view) ]

urls = []
current_path = []

urlpatterns.append(path('', handle_main))
urlpatterns.append(path('category/<str:category>', handle_category))
urlpatterns.append(path('article/<str:article_url>', handle_article))
urlpatterns.append(path('users/<str:username>/', handle_user))

urlpatterns.append(path('register/', handle_register, name='register'))
urlpatterns.append(path('login/', handle_login, name='login'))
urlpatterns.append(path('logout/', handle_logout, name='logout'))

urlpatterns.append(path('editor/<str:article_url>/', handle_editor, name='editor'))
urlpatterns.append(path('editor/', handle_editor, name='editor'))

handler404 = handle_404
handler500 = handle_500

print("urls:", urls)
