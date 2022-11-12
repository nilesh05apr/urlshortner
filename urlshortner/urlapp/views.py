from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect

from urlapp.forms import URLForm
from urlapp.util import checkHash
from .models import URLS
from rest_framework.decorators import api_view


# Create your views here.

def health(request):
    return JsonResponse({'status':'ok'})

@api_view(['POST'])
def api(request):
    if request.method == 'POST':
        long_url = request.data['long_url']
        short_url = checkHash(long_url=long_url)
        surl = 'https://surl.herokuapp.com/api'+short_url
        return JsonResponse({"long_url":long_url,"short_url":surl})
    else:
        return JsonResponse({"error":"Invalid Request"})


        


def reroute(request,pk):
    url_data = URLS.objects.get(id=pk)
    return redirect(url_data.long_url)
    