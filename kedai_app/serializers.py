from rest_framework import serializers
from .models import *
from .const import *

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
    time_now = datetime.datetime.now().time()
    waktu_pemesanan = serializers.TimeField(default=time_now)
    id_menu_harian = serializers.PrimaryKeyRelatedField(
      queryset= MenuHarian.objects.all())

    class Meta:
        model = Pesanan
        fields = '__all__'
        #depth = 1

    #validasi waktu pemesanan
    def validate_waktu_pemesanan(self,value):
        if value < MIN_TIME or value > MAX_TIME:
            raise serializers.ValidationError("tidak bisa memesan di luar jam pemesanan (07.00 - 10.00)")
        return value

    #validasi tanggal pemesanan pada menu
    def validate_id_menu_harian(self,value):
        date_today = datetime.datetime.today()
        menu_pesanan = MenuHarian.objects.get(id_menu_harian=value.id_menu_harian)
        menu_harian_today = MenuHarian.objects.filter(tanggal=date_today)
        if menu_pesanan not in menu_harian_today:
            raise serializers.ValidationError("Menu tidak tersedia pada hari ini")
        return value

class PesananCustSerializer(PesananSerializer):
    class Meta:
        model = Pesanan
        fields = ['waktu_pemesanan','id_menu_harian','jumlah_pesanan','status_pesanan','id_pelanggan']


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
        fields = ['nama_menu','harga_menu','deskripsi_menu','foto_menu']

class MenuHarianSerializer(serializers.ModelSerializer):
    id_menu = serializers.PrimaryKeyRelatedField(
      queryset= Menu.objects.all(), source='menu')
    detail_menu = DetailMenuSerializer(read_only=True,source='menu') #serializers.SlugRelatedField(slug_field='id_menu',queryset= Menu.objects.all())
    class Meta:
        model = MenuHarian
        fields = ['id_menu_harian','tanggal','id_menu','detail_menu']
        #depth = 1

class MenuTest(serializers.ModelSerializer):
    class Meta:
        model = MenuHarian
        fields = '__all__'
        depth = 1


class DetailMenuPesananSerializer(serializers.ModelSerializer):
    id_menu = serializers.PrimaryKeyRelatedField(
      queryset= Menu.objects.all(), source='menu')
    nama_menu = serializers.StringRelatedField(source='menu')

    class Meta:
        model = MenuHarian
        fields = ['id_menu','nama_menu']


class DetailPesananPelangganSerializer(serializers.ModelSerializer):
    menu = DetailMenuPesananSerializer(read_only=True,source='id_menu_harian')
    class Meta:
        model = Pesanan
        fields = ['menu','jumlah_pesanan','status_pesanan']
        depth = 1


class PesananPelanggan(serializers.ModelSerializer):
    pesanan = DetailPesananPelangganSerializer(read_only=True,many=True)
    class Meta:
        model = Pelanggan
        fields =  '__all__'
        depth = 1

