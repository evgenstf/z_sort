from django.http import HttpResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt


from html_factories.category import CategoryHtmlFactory

@csrf_exempt
def handle_url(request, category):
    template = Template(CategoryHtmlFactory.create(category))
    context = Context({'request': request})
    return HttpResponse(template.render(context))
