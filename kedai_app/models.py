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


class Kurir(models.Model):
    id_kurir = models.AutoField(primary_key=True)
    nama_kurir = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'kurir'


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


class MenuHarian(models.Model):
    tanggal = models.DateField()
    id_menu_harian = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu')

    class Meta:
        managed = False
        db_table = 'menu_harian'


class Pelanggan(models.Model):
    nama_pelanggan = models.CharField(max_length=50)
    id_pelanggan = models.AutoField(primary_key=True)
    id_gedung = models.ForeignKey(Gedung, models.DO_NOTHING, db_column='id_gedung')
    no_hp_pelanggan = models.CharField(max_length=15)
    keterangan_lokasi = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pelanggan'


class Pesanan(models.Model):
    id_pelanggan = models.ForeignKey(Pelanggan, models.DO_NOTHING, db_column='id_pelanggan')
    id_menu_harian = models.ForeignKey(MenuHarian, models.DO_NOTHING, db_column='id_menu_harian')
    id_pesanan = models.AutoField(primary_key=True)
    waktu_pemesanan = models.TimeField()
    jumlah_pesanan = models.IntegerField()
    status_pesanan = models.CharField(max_length=16)
    id_cs = models.ForeignKey(CustomerService, models.DO_NOTHING, db_column='id_cs', blank=True, null=True)
    id_kurir = models.ForeignKey(Kurir, models.DO_NOTHING, db_column='id_kurir', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pesanan'


class Suplier(models.Model):
    nama_suplier = models.CharField(max_length=50)
    alamat_suplier = models.CharField(max_length=100)
    id_suplier = models.SmallIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'suplier'
