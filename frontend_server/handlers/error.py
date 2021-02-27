from django.http import HttpResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt

from html_factories.error import ErrorHtmlFactory

@csrf_exempt
def handle_404(request, exception):
    template = Template(ErrorHtmlFactory.create('404'))
    context = Context({'request': request})
    return HttpResponse(template.render(context))
#
@csrf_exempt
def handle_500(request, *args, **argv):
    template = Template(ErrorHtmlFactory.create('500'))
    context = Context({'request': request})
    return HttpResponse(template.render(context))
