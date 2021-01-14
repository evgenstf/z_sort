from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import settings

import simplejson as json

from html_factories.base import BaseHtmlFactory
from html_factories.category import CategoryHtmlFactory
from html_factories.main import MainHtmlFactory
from html_factories.editor import EditorHtmlFactory

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


def handle_article_request(path):
    article = get_article_by_path(path)
    content_html = open(article['content_html'], 'r').read()
    js = open(article['js'], 'r').read()
    css = open(article['css'], 'r').read()

    template = Template(BaseHtmlFactory.create_from_content(content_html, js, css))
    return HttpResponse(template.render(Context({})))

def handle_main_request(meta):
    template = Template(MainHtmlFactory.create_from_meta(meta))
    return HttpResponse(template.render(Context({})))

def handle_category_request(path):
    template = Template(CategoryHtmlFactory.create_from_meta(get_meta_by_path(path), path))
    return HttpResponse(template.render(Context({})))

def handle_editor_request(request):
    editor_html = ''
    js = ''
    css = ''
    template = Template(EditorHtmlFactory.create(editor_html, js, css))
    if len(request.POST):
        print(request.POST.dict())
    return HttpResponse(template.render(Context({})))

def handle_url(request):
    path = request.path.strip('/').split('/') if request.path != '/' else []
    print('path:', path)
    meta = get_meta_by_path(path)
    print('meta:', meta)

    if path == ['editor']:
        return handle_editor_request(request)

    if meta['type'] == 'article':
        return handle_article_request(path)
    elif meta['type'] == 'category':
        return handle_category_request(path)
    elif meta['type'] == 'main':
        return handle_main_request(meta)
