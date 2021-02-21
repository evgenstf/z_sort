from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template, Context, RequestContext
from django.views.decorators.csrf import csrf_exempt

from html_factories.login import LoginHtmlFactory
from html_factories.register import RegisterHtmlFactory

@csrf_exempt
def handle_login(request):
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


@csrf_exempt
def handle_register(request):
    if request.user.is_authenticated:
        return redirect('editor')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,user + ', welcome to Z-SORT!')
                return redirect('login')

        context = {'form': form}
        template = Template(RegisterHtmlFactory.create())
        return HttpResponse(template.render(Context(context)))

@csrf_exempt
def handle_logout(request):
    logout(request)
    return redirect('login')

