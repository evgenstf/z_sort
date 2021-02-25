from django.http import HttpResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def handle_404(request, exception):
    template = Template(Error404HtmlFactory.create())
    context = Context({'request': request})
    print("::::::::::")
    return HttpResponse(template.render(context))
