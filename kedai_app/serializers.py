from rest_framework import serializers
from .models import *
import datetime

class GedungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gedung
        fields = '__all__'
        depth = 1

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = '__all__'
        #depth = 1

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = '__all__'
        #depth = 1

    def validate_waktu_pemesanan(self,value):
        print("cek waktu")
        LOW_TIME = datetime.time(7,0,0)
        HIGH_TIME = datetime.time(10,0,0)

        if value < LOW_TIME or value > HIGH_TIME:
            raise serializers.ValidationError("tidak bisa memesan di luar jam pemesanan (07.00 - 10.00)")

        return value

class SuplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suplier
        fields = '__all__'
        depth = 1

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        #depth = 1

class DetailMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['nama_menu','harga_menu','deskripsi_menu']

class MenuHarianSerializer(serializers.ModelSerializer):
    id_menu = serializers.PrimaryKeyRelatedField(
      queryset= Menu.objects.all(), source='menu')
    detail_menu = DetailMenuSerializer(read_only=True,source='menu') #serializers.SlugRelatedField(slug_field='id_menu',queryset= Menu.objects.all())
    class Meta:
        model = MenuHarian
        fields = ['id_menu_harian','tanggal','id_menu','detail_menu']
        #depth = 1
