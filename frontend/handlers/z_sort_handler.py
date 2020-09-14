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

def get_article_by_id(article_id):
    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sock.send(json.dumps({"type": 'article', "id": article_id}).encode())
    response = sock.recv(100000).decode("utf-8")
    sock.close()
    return json.loads(response)

def get_all_article_previews():
    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sock.send(json.dumps({"type": 'all_article_previews'}).encode())
    response = sock.recv(100000).decode("utf-8")
    sock.close()
    return json.loads(response)


def index(request):
    return HttpResponse(ArticlePreviewsHtmlFactory.create_from_content(get_all_article_previews()))

@csrf_exempt
def article(request, article_id):
    template = Template(ArticleHtmlFactory.create_from_article(get_article_by_id(article_id)))
    return HttpResponse(template.render(Context({})))
