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
from html_compiler.html_factories.article_preview import ArticlePreviewHtmlFactory

import multiprocessing as mp

from storage.sql_article_connector import SQLArticleConnector

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

    @staticmethod
    def publish(article_json):
        article_json['id'] = SQLArticleConnector.get_next_article_id()
        article_json['url'] = 'article_' + str(article_json['id'])

        article_json['preview_html'] = ArticlePreviewHtmlFactory.build_html(article_json)

        compilation_result = Editor.compile_article(article_json)

        article_json['html'] = compilation_result['html']
        article_json['js'] = compilation_result['js']
        article_json['css'] = compilation_result['css']

        article_json['header'] = json.dumps(article_json['header'])
        article_json['authors'] = json.dumps(article_json['authors'])
        article_json['sections'] = json.dumps(article_json['sections'])
        article_json['tags'] = ''

        SQLArticleConnector.add_new_article(article_json)

        return article_json['url']

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

        elif type == 'publish':
            url = Editor.publish(received_json['article'])
            return JsonResponse({'url': url})


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
