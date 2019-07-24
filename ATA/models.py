from django.db import models

# Create your models here.

# class Blog(request):
#     foto =
#     deskripsi =
#     link = 


class Mentee(models.Model):
    profil = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    quotes = models.CharField(max_length=100)


class Mentor(models.Model):
    profil = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    quotes = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

class Blog(models.Model):
    judul = models.CharField(max_length=100)
    tanggal = models.DateField()
    comment = models.CharField(max_length=1000)
    foto = models.CharField(max_length=100)
    deskripsi = models.TextField()