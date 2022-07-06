from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from urlapp.forms import URLForm
from urlapp.util import checkHash

# Create your views here.

def index(request):
    return HttpResponse("Index")

def upload(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            #print(form['long_url'])
            long_url = form['long_url'].value()
            short_url = checkHash(long_url=long_url)
            print(short_url)
            print(long_url)
            # return HttpResponse(short_url)
            return JsonResponse({"long_url":long_url,"short_url":short_url})
    else:
        form = URLForm()
    return render(request,"urlapp/form.html",{"form":form})