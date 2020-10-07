from django.shortcuts import render
from django.conf import settings
from .models import Surat, Qory, Murottal


def Player(request):
    dari = request.POST["AyatPertama"]
    ke = request.POST["AyatTerakhir"]
    surat = request.POST["surah"]
    syekh = request.POST["syekh"]

    x = []
    for i in range(int(dari), int(ke) + 1):
        x.append(i)
    x = Murottal.objects.filter(surat__no_surat=int(surat), ayat__no_ayat__in=x, qory__pk=syekh)
    hasil = []
    for item in x:
        hasil.append({
            'title': '%s' % item.ayat,
            'file': '%s%s%s' % (settings.SITE_URL, settings.MEDIA_URL, item.sound)
        })

    data = {
        'playlist': hasil
    }

    return render(request, 'index.html', data)


def Home(request):
    syekh = Qory.objects.all()
    surat = Surat.objects.all()

    data = {
        'syekh': syekh,
        'surah': surat,
    }
    return render(request, 'home.html', data)
