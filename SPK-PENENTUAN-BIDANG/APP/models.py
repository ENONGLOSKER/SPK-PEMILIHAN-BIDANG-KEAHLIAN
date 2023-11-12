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
    gap  = models.FloatField()
    
    def __str__(self):
        return str(self.nilai)
#penilaian
class Penilaian(models.Model):
    penilaian_alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE)
    penilaian_kriteria1 = models.IntegerField(default=0)
    penilaian_kriteria2 = models.IntegerField(default=0)
    penilaian_kriteria3 = models.IntegerField(default=0)
    penilaian_kriteria4 = models.IntegerField(default=0)
    penilaian_kriteria5 = models.IntegerField(default=0)

    def __str__(self):
        return str(self.penilaian_alternatif)
