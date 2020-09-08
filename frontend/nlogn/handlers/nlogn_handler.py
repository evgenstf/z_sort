from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from nlogn import settings

import simplejson as json

def index(request):
    return render(request, "index.html")

@csrf_exempt
def article(request, article_url):
    import socket

    sock = socket.socket()
    sock.connect(('localhost', 9999))


    sock.send(json.dumps({"id": article_url}).encode())
    response = sock.recv(100000).decode("utf-8")
    sock.close()

    return HttpResponse(response)
