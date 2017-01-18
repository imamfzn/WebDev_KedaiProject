# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CustomerService(models.Model):
    id_cs = models.AutoField(primary_key=True)
    nama_cs = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'customer_service'

    def __str__(self):
        return self.nama_cs


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Gedung(models.Model):
    nama_gedung = models.CharField(max_length=50)
    id_gedung = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gedung'

    def __str__(self):
        return self.nama_gedung


class Kurir(models.Model):
    id_kurir = models.AutoField(primary_key=True)
    nama_kurir = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'kurir'

    def __str__(self):
        return self.nama_kurir


class Menu(models.Model):
    nama_menu = models.CharField(max_length=50)
    harga_menu = models.IntegerField()
    id_menu = models.AutoField(primary_key=True)
    id_suplier = models.ForeignKey('Suplier', models.DO_NOTHING, db_column='id_suplier')
    deskripsi_menu = models.TextField(blank=True, null=True)
    foto_menu = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'

    def __str__(self):
        return self.nama_menu


class MenuHarian(models.Model):
    tanggal = models.DateField()
    id_menu_harian = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu')

    class Meta:
        managed = False
        db_table = 'menu_harian'

    def __str__(self):
        return '%s' % (self.menu)


class Pelanggan(models.Model):
    nama_pelanggan = models.CharField(max_length=50)
    id_pelanggan = models.AutoField(primary_key=True)
    id_gedung = models.ForeignKey(Gedung, models.DO_NOTHING, db_column='id_gedung')
    no_hp_pelanggan = models.CharField(max_length=15)
    keterangan_lokasi = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pelanggan'


    def __str__(self):
        return self.nama_pelanggan


class Pesanan(models.Model):
    STATUS_PESANAN_CHOICES = (
        ('belum konfirmasi','belum konfirmasi'),
        ('batal','batal'),
        ('sudah konfirmasi','sudah konfirmasi'),
        ('sudah dicetak','sudah dicetak')
    )
    id_pelanggan = models.ForeignKey(Pelanggan, models.DO_NOTHING, db_column='id_pelanggan',related_name='pesanan')
    id_menu_harian = models.ForeignKey(MenuHarian, models.DO_NOTHING, db_column='id_menu_harian')
    id_pesanan = models.AutoField(primary_key=True)
    waktu_pemesanan = models.TimeField(auto_now_add=True)
    jumlah_pesanan = models.IntegerField()
    status_pesanan = models.CharField(max_length=16, choices=STATUS_PESANAN_CHOICES, default='belum konfirmasi')
    id_cs = models.ForeignKey(CustomerService, models.DO_NOTHING, db_column='id_cs', blank=True, null=True)
    id_kurir = models.ForeignKey(Kurir, models.DO_NOTHING, db_column='id_kurir', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pesanan'

    def __str__(self):
        return '%s %s' % (self.id_pelanggan,self.waktu_pemesanan)


class Suplier(models.Model):
    nama_suplier = models.CharField(max_length=50)
    alamat_suplier = models.CharField(max_length=100)
    id_suplier = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'suplier'

    def __str__(self):
        return self.nama_suplier
