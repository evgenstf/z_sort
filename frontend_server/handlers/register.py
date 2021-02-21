from .forms import CreateUserForm

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template, Context, RequestContext
from django.views.decorators.csrf import csrf_exempt

from html_factories.register import RegisterHtmlFactory

@csrf_exempt
def handle_url(request):
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

