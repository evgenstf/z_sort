from django.http import HttpResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt


from html_factories.main import MainHtmlFactory

@csrf_exempt
def handle_url(request):
    template = Template(MainHtmlFactory.create())
    context = Context({'request': request})
    return HttpResponse(template.render(context))
