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

from handlers import z_sort_handler

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [ path('favicon.ico', favicon_view) ]

urls = []
current_path = []

def discover_urls(path_tree):
    current_url = '/'.join(current_path) + ('/' if len(current_path) else '')
    urls.append(current_url)

    if not path_tree:
        return
    for node_name, node_tree in path_tree.items():
        current_path.append(node_name)
        discover_urls(node_tree)
        current_path.pop()

def get_all_urls():
    import socket
    import json

    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sock.send(json.dumps({"type": 'path_tree'}).encode())
    response = sock.recv(100000).decode("utf-8")
    sock.close()
    return discover_urls(json.loads(response))

get_all_urls()

for url in urls:
    urlpatterns.append(path(url, z_sort_handler.handle_url))

urlpatterns.append(path('register/', z_sort_handler.register_page, name='register'))
urlpatterns.append(path('login/', z_sort_handler.login_page, name='login'))
urlpatterns.append(path('logout/', z_sort_handler.logout_user, name='logout'))
urlpatterns.append(path('editor/', z_sort_handler.handle_editor_request, name='editor'))

print("urls:", urls)


