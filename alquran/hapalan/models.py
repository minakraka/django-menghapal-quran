from django.db import models

class Surat(models.Model):
    no_surat = models.IntegerField()
    nama_surat = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_surat

class Ayat(models.Model):
    no_ayat = models.IntegerField()
    surat = models.ForeignKey(Surat, on_delete=models.CASCADE)

    def __str__(self):
        return "Surat %s - Ayat %s" % (self.surat, self.no_ayat)

class Syekh(models.Model):
    nama = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Murottal(models.Model):
    syekh = models.ForeignKey(Syekh, on_delete=models.CASCADE)
    surat = models.ForeignKey(Surat, on_delete=models.CASCADE)
    ayat = models.ForeignKey(Ayat, on_delete=models.CASCADE)
    sound = models.CharField(max_length=100)

    def __str__(self):
        return str(self.surat)