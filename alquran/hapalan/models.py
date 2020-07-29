from django.db import models

# Create your models here.
class Surat(models.Model):
    no_surat = models.IntegerField(primary_key=True)
    nama_surat = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_surat

class Ayat(models.Model):
    no_ayat = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=100)
    surat = models.ForeignKey(Surat, on_delete=models.CASCADE)

    def __str__(self):
        return self.no_ayat

class Qory(models.Model):
    nama = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)

    def __str__(self):
        return self.nama