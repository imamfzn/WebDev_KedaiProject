# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id_cs', models.AutoField(primary_key=True, serialize=False)),
                ('nama_cs', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'customer_service',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='Gedung',
            fields=[
                ('nama_gedung', models.CharField(max_length=50)),
                ('id_gedung', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'gedung',
            },
        ),
        migrations.CreateModel(
            name='Kurir',
            fields=[
                ('id_kurir', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kurir', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'kurir',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('nama_menu', models.CharField(max_length=50)),
                ('harga_menu', models.IntegerField()),
                ('id_menu', models.AutoField(primary_key=True, serialize=False)),
                ('deskripsi_menu', models.TextField(blank=True, null=True)),
                ('foto_menu', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='MenuHarian',
            fields=[
                ('tanggal', models.DateField()),
                ('id_menu_harian', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'menu_harian',
            },
        ),
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('nama_pelanggan', models.CharField(max_length=50)),
                ('id_pelanggan', models.AutoField(primary_key=True, serialize=False)),
                ('no_hp_pelanggan', models.CharField(max_length=15)),
                ('keterangan_lokasi', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'pelanggan',
            },
        ),
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('id_pesanan', models.AutoField(primary_key=True, serialize=False)),
                ('waktu_pemesanan', models.TimeField()),
                ('jumlah_pesanan', models.IntegerField()),
                ('status_pesanan', models.CharField(max_length=16)),
            ],
            options={
                'managed': False,
                'db_table': 'pesanan',
            },
        ),
        migrations.CreateModel(
            name='Suplier',
            fields=[
                ('nama_suplier', models.CharField(max_length=50)),
                ('alamat_suplier', models.CharField(max_length=100)),
                ('id_suplier', models.SmallIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'suplier',
            },
        ),
    ]
