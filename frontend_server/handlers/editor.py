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

import multiprocessing as mp

def compile_article_in_another_process(article_json, result_queue):
    result_queue.put(compile_article(article_json))


class Editor:
    @staticmethod
    def compile_article(article_json):
        try:
            ctx = mp.get_context('spawn')
            result_queue = ctx.Queue()
            compile_process = ctx.Process(
                    target=compile_article_in_another_process,
                    args=(article_json, result_queue,))
            compile_process.start()
            result = result_queue.get()
            compile_process.join()
            return result

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
