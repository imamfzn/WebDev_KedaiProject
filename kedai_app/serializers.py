from rest_framework import serializers
from .models import *

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

class MenuHarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuHarian
        fields = '__all__'
        depth = 1

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

class MenuCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id_menu','nama_menu','harga_menu','deskripsi_menu']