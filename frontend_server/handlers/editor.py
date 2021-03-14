from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from html_factories.editor import EditorHtmlFactory

import socket
import json

import sys

from storage.sql_article_connector import SQLArticleConnector

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

def handle_post_request(request, article_url):
    try:
        body_unicode = request.body.decode('utf-8')
        print("received body_unicode:", body_unicode)
        received_json = json.loads(json.loads(body_unicode))

        print("received post request:", received_json)

        for key, value in received_json.items():
            print("key:", key, "value:", value)
        print("received post request:", received_json)

        type = received_json['type']
        print("type:", type)
        if type == 'compile':
            result = compile_article(received_json['sections'])
            template = Template('{% load static %}\n' + json.loads(result)['result'])
            rendered_page = template.render(Context({}))

            return JsonResponse({'result': rendered_page})

        if type == 'get_sections':
            print("return sections")
            return JsonResponse({'result': []})

    except Exception as ex:
        print("Unexpected error:", ex)

@csrf_exempt
@login_required(login_url='login')
def handle_editor(request, article_url=''):
    if (request.method == "POST"):
        return handle_post_request(request, article_url)

    template = Template(EditorHtmlFactory.create('', '', ''))

    context = Context({'request': request})
    return HttpResponse(template.render(context))

