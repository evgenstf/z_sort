from django.http import HttpResponse
from django.template import Template, Context, RequestContext

from django.views.decorators.csrf import csrf_exempt

from html_factories.user_page import UserPageHtmlFactory

@csrf_exempt
def handle_user_page(request, username):
    articles_num, user_page_html = UserPageHtmlFactory.create(username)
    template = Template(user_page_html)
    context = Context({
        'request': request,
        'owner': request.path.split('/')[-2],
        'articles_num': articles_num,
        'is_it_owner': request.path.split('/')[-2] == str(request.user),
    })
    return HttpResponse(template.render(context))