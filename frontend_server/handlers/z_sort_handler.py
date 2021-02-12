from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Template, Context, RequestContext

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import settings

import simplejson as json

from html_factories.base import BaseHtmlFactory
from html_factories.category import CategoryHtmlFactory
from html_factories.main import MainHtmlFactory
from html_factories.editor import EditorHtmlFactory
from html_factories.login import LoginHtmlFactory
from html_factories.register import RegisterHtmlFactory

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

import socket

def get_article_by_path(path):
    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sock.send(json.dumps({"type": 'article', "path": path}).encode())
    response = sock.recv(1000000).decode("utf-8")
    sock.close()
    print("response length:", len(response))
    return json.loads(response)

def get_meta_by_path(path):
    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sock.send(json.dumps({"type": 'meta', "path": path}).encode())
    response = sock.recv(1000000).decode("utf-8")
    sock.close()
    return json.loads(response)


def handle_article_request(path, request):
    article = get_article_by_path(path)
    content_html = open(article['content_html'], 'r').read()
    js = open(article['js'], 'r').read()
    css = open(article['css'], 'r').read()

    template = Template(BaseHtmlFactory.create_from_content(content_html, js, css))
    context = Context({'request': request})
    return HttpResponse(template.render(context))

def handle_main_request(meta, request):
    template = Template(MainHtmlFactory.create_from_meta(meta))
    context = Context({'request': request})
    return HttpResponse(template.render(context))

def handle_category_request(path, request):
    template = Template(CategoryHtmlFactory.create_from_meta(get_meta_by_path(path), path))
    context = Context({'request': request})
    return HttpResponse(template.render(context))

def update_article_from_editor(article_to_update):
    sock = socket.socket()
    sock.connect(('localhost', 9996))
    sock.send(json.dumps({"type": "update_meta", "new_meta": article_to_update[0], "article_id": "editor_result"}).encode())
    sock.close()
    sock = socket.socket()
    sock.connect(('localhost', 9996))
    sock.send(json.dumps({"type": "update_sections", "new_sections": article_to_update[1:], "article_id": "editor_result"}).encode())
    sock.close()
    sock = socket.socket()
    sock.connect(('localhost', 9996))
    sock.send(json.dumps({"type": "compile", "article_id": "editor_result"}).encode())
    sock.close()
    sock = socket.socket()
    sock.connect(('localhost', 9996))
    sock.send(json.dumps({"type": "get", "article_id": "editor_result"}).encode())
    result = sock.recv(1000000)
    sock.close()
    return result

@csrf_exempt
@login_required(login_url='login')
def handle_editor_request(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        result = update_article_from_editor(received_json)

        template = Template('{% load static %}\n' + json.loads(result)['result'])
        rendered_page = template.render(Context({}))

        return JsonResponse({'result': rendered_page})

    path = ['editor', 'editor_result']
    editing_article = get_article_by_path(path)
    content_html = open(editing_article['content_html'], 'r').read()
    js = ''
    css = ''
    template = Template(EditorHtmlFactory.create(content_html, js, css))

    context = Context({'request': request})
    return HttpResponse(template.render(context))

@csrf_exempt
def handle_url(request):
    path = request.path.strip('/').split('/') if request.path != '/' else []
    print('path:', path)
    meta = get_meta_by_path(path)
    print('meta:', meta)

    if meta['id'] == 'editor':
        return handle_editor_request(request)

    if meta['type'] == 'article':
        return handle_article_request(path, request)
    elif meta['type'] == 'category':
        return handle_category_request(path, request)
    elif meta['type'] == 'main':
        return handle_main_request(meta, request)

@csrf_exempt
def register_page(request):
    if request.user.is_authenticated:
        return redirect('editor')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,user + ', welcome to Z-SORT!')
                return redirect('login')

        context = {'form': form}
        template = Template(RegisterHtmlFactory.create())
        return HttpResponse(template.render(Context(context)))

@csrf_exempt
def login_page(request):
    if request.user.is_authenticated:
        return redirect('editor')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('editor')
            else:
                messages.info(request, 'Incorrect username or password')

        context = Context({'request': request})
        template = Template(LoginHtmlFactory.create())
        return HttpResponse(template.render(context))

@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('login')
