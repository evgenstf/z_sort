from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from html_factories.editor import EditorHtmlFactory

import socket
import json

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

@csrf_exempt
@login_required(login_url='login')
def handle_editor(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        result = update_article_from_editor(received_json)

        template = Template('{% load static %}\n' + json.loads(result)['result'])
        rendered_page = template.render(Context({}))

        return JsonResponse({'result': rendered_page})

    editing_article = SQLArticleConnector.get_article_by_id(1)
    content_html = editing_article['html']
    template = Template(EditorHtmlFactory.create(content_html, editing_article['js'], ''))

    context = Context({'request': request})
    return HttpResponse(template.render(context))

