from django.http import HttpResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt


from html_factories.article import ArticleHtmlFactory

@csrf_exempt
def handle_url(request, article_url):
    template = Template(ArticleHtmlFactory.create(article_url))
    context = Context({'request': request})
    return HttpResponse(template.render(context))
