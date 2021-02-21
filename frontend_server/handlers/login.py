from .forms import CreateUserForm

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template, Context, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from html_factories.login import LoginHtmlFactory

@csrf_exempt
def handle_url(request):
    if request.user.is_authenticated:
        return redirect('editor')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('editor')
            else:
                messages.info(request, 'Incorrect username or password')

        context = Context({'request': request})
        template = Template(LoginHtmlFactory.create())
        return HttpResponse(template.render(context))
