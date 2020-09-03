from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from urlshortener.db import get_hash_by_url, get_url_by_hash
from urlshortener import settings

import simplejson as json


def index(request):
    return render(request, "index.html")

def redirect_to_google(request):
    return redirect('https://google.com')

@csrf_exempt
def short_url(request):
    url = request.POST.get('url')
    print("get url:", url)
    hash_url = get_hash_by_url(url)
    print("hash_url:", hash_url)
    result_url = settings.SITE_NAME + 'r/' + hash_url
    print("result:", result_url)
    return HttpResponse(json.dumps({"short_url": result_url}), content_type="application/json")

def redirect_from_short(request, short_url):
    full_url = get_url_by_hash(short_url)
    print("short_url:", short_url)
    print("full_url:", full_url)
    return redirect(full_url)
