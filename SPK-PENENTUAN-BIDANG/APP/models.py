from django.db import models

# Create your models here.
# alternatif
class Alternatif(models.Model):
    nama_alternatif = models.CharField(max_length=50, unique=True)
    simbol          = models.CharField(max_length=5, unique=True)
    nim             = models.CharField(max_length=12, unique=True)
    alamat          = models.TextField()

    def __str__(self):
        return str(self.nama_alternatif)
#kriteria
class Kriteria(models.Model):
    nama_kriteria = models.CharField(max_length=50, unique=True)
    nilai_target  = models.IntegerField()
    
    def __str__(self):
        return str(self.nama_kriteria)
#gap
class Gap(models.Model):
    nilai = models.IntegerField()
    gap  = models.IntegerField()
    
    def __str__(self):
        return str(self.nilai)
#penilaian
