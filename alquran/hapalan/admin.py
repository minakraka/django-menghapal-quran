from django.contrib import admin
from .models import Qory, Surat, Ayat, Murottal

# Register your models here.
class SuratAdmin(admin.ModelAdmin):
    list_display = ('no_surat', 'nama_surat')
admin.site.register(Surat, SuratAdmin)

class AyatAdmin(admin.ModelAdmin):
    search_fields = ('surat',)
    list_display = ('no_ayat', 'surat')
admin.site.register(Ayat, AyatAdmin)

class QoryAdmin(admin.ModelAdmin):
    list_display = ('nama', 'profile')
admin.site.register(Qory, QoryAdmin)

class MurottalAdmin(admin.ModelAdmin):
    list_display = ('qory', 'ayat', 'sound')
    autocomplete_fields = ('ayat',)
admin.site.register(Murottal, MurottalAdmin)
