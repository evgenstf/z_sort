from django.http import HttpResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt

from html_factories.error import Error404HtmlFactory
from html_factories.error import Error500HtmlFactory

@csrf_exempt
def handle_404(request, exception):
    template = Template(Error404HtmlFactory.create())
    context = Context({'request': request})
    return HttpResponse(template.render(context))

@csrf_exempt
def handle_500(request, *args, **argv):
    template = Template(Error500HtmlFactory.create())
    context = Context({'request': request})
    return HttpResponse(template.render(context))
