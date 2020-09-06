from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json


def home(request):
    # return HttpResponse("Sisil")
    data = open(settings.MEDIA_URL + 'data.json') # warna orange nama dari json yang dipanggil
    data = json.load(data) # data sbg  fungsinya digunakan u memanggil fungsi murottal
    
    return render(request, 'index.html', data)