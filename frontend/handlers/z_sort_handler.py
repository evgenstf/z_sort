from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import settings

import simplejson as json

from html_factories.article_previews import ArticlePreviewsHtmlFactory
from html_factories.article import ArticleHtmlFactory

import socket

def get_article_by_path(path):
    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sock.send(json.dumps({"type": 'article', "path": path}).encode())
    response = sock.recv(100000).decode("utf-8")
    sock.close()
    return json.loads(response)

def get_meta_by_path(path):
    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sock.send(json.dumps({"type": 'meta', "path": path}).encode())
    response = sock.recv(100000).decode("utf-8")
    sock.close()
    return json.loads(response)


def handle_article_request(path):
    template = Template(ArticleHtmlFactory.create_from_article(get_article_by_path(path)))
    return HttpResponse(template.render(Context({})))

def handle_main_request(meta):
    template = Template(MainHtmlFactory.create_from_meta(meta))
    return HttpResponse(template.render(Context({})))

def handle_category_request(meta):
    template = Template(ArticleHtmlFactory.create_from_article(get_article_by_path(path)))
    return HttpResponse(template.render(Context({})))

def handle_url(request):
    path = request.path.strip('/').split('/') if request.path != '/' else []
    meta = get_meta_by_path(path)
    print('meta:', meta)
    if meta['type'] == 'article':
        return handle_article_request(path)
    elif meta['type'] == 'category':
        return handle_category_request(path)
    elif meta['type'] == 'main':
        return handle_main_request(meta)
