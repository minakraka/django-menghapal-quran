from django.shortcuts import render
from django.conf import settings
from .models import Surat, Syekh, Murottal


def Player(request):
    dari = request.POST["AyatPertama"]
    ke = request.POST["AyatTerakhir"]
    surat = request.POST["surah"]
    syekh = request.POST["syekh"]

    temp = []
    for i in range(int(dari), int(ke) + 1):
        temp.append(i)

    object = Murottal.objects.filter(surat__no_surat=int(surat), ayat__no_ayat__in=temp, syekh__pk=syekh)
    hasil = []
    for item in object:
        hasil.append({
            'title': '%s' % item.ayat,
            'file': '%s%s%s' % (settings.SITE_URL, settings.MEDIA_URL, item.sound)
        })

    data = {
        'playlist': hasil
    }

    return render(request, 'index.html', data)


def Home(request):
    syekh = Syekh.objects.all()
    surat = Surat.objects.all()

    data = {
        'syekh': syekh,
        'surah': surat,
    }
    return render(request, 'home.html', data)
