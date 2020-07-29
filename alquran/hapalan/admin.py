from django.contrib import admin
from .models import Qory, Surat, Ayat

# Register your models here.
class SuratAdmin(admin.ModelAdmin):
    list_display = ('no_surat', 'nama_surat')
admin.site.register(Surat, SuratAdmin)

class AyatAdmin(admin.ModelAdmin):
    list_display = ('no_ayat', 'url', 'surat')
admin.site.register(Ayat, AyatAdmin)

class QoryAdmin(admin.ModelAdmin):
    list_display = ('nama', 'profile')
admin.site.register(Qory, QoryAdmin)
