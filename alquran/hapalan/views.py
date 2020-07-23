from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json


def home(request):
    # return HttpResponse("Sisil")
    data = open(settings.MEDIA_URL + 'data.json')
    data = json.load(data)
    
    return render(request, 'index.html', data)