from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from html_factories.editor import EditorHtmlFactory


import socket
import json

import sys

from html_compiler.compile import compile_article


class Editor:
    @staticmethod
    def compile_article(article_json):
        try:
            return compile_article(article_json)
        except Exception as e:
            print("[error] Exception:", e)
            return '<br><br><br><br>ERROR'

def handle_post_request(request, article_url):
    try:
        body_unicode = request.body.decode('utf-8')
        print("received body_unicode:", body_unicode)
        received_json = json.loads(json.loads(body_unicode))

        print("received post request:", received_json)

        type = received_json['type']
        print("type:", type)

        if type == 'compile':
            article_json = received_json['article']
            result = Editor.compile_article(article_json)
            template = Template(result['html'])
            result['html'] = template.render(Context({}))

            return JsonResponse(result)

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
