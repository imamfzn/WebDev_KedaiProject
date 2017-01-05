from rest_framework import viewsets
from .models import *
from .serializers import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class PelangganViewSet(viewsets.ModelViewSet):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer

class GedungViewSet(viewsets.ModelViewSet):
    queryset = Gedung.objects.all()
    serializer_class = GedungSerializer

class PesananViewSet(viewsets.ModelViewSet):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer

class SuplierViewSet(viewsets.ModelViewSet):
    queryset = Suplier.objects.all()
    serializer_class = SuplierSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuHarianViewSet(viewsets.ModelViewSet):
    queryset = MenuHarian.objects.all()
    serializer_class = MenuHarianSerializer