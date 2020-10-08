from django.contrib import admin
from .models import Syekh, Surat, Ayat, Murottal


class SuratAdmin(admin.ModelAdmin):
    list_display = ('no_surat', 'nama_surat')
admin.site.register(Surat, SuratAdmin)


class AyatAdmin(admin.ModelAdmin):
    search_fields = ('surat',)
    list_display = ('no_ayat', 'surat')
admin.site.register(Ayat, AyatAdmin)


class SyekhAdmin(admin.ModelAdmin):
    list_display = ('nama', 'profile')
admin.site.register(Syekh, SyekhAdmin)


class MurottalAdmin(admin.ModelAdmin):
    list_display = ('syekh', 'ayat', 'sound')
    autocomplete_fields = ('ayat',)
admin.site.register(Murottal, MurottalAdmin)
