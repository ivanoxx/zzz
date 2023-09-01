from django.db import models

class MyItem(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_tambah = models.DateField(auto_now_add=True)
    harga = models.IntegerField()
    deskripsi = models.TextField()
