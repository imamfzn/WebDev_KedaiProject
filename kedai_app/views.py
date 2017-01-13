from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from .const import *
from .permissions import *
import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ServerTime(APIView):
    def get(self,request):
        result = {
            'date' : datetime.datetime.now().date(),
            'time' : datetime.datetime.now().time()
        }
        return Response(result)

class PelangganViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyCustomer]
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer

class GedungViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomerServiceLow]
    queryset = Gedung.objects.all()
    serializer_class = GedungSerializer

class PesananViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyCustomerService]
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer

class PesananCustViewSet(viewsets.ModelViewSet):
    permission_classes = [PesananPermission]
    queryset = Pesanan.objects.all()
    serializer_class = PesananCustSerializer

class SuplierViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyCustomerService]
    queryset = Suplier.objects.all()
    serializer_class = SuplierSerializer

class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomerServiceLow]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuHarianViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyCustomerService]
    queryset = MenuHarian.objects.all()
    serializer_class = MenuHarianSerializer

class MenuPelangganViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomerServiceLow]
    time_now = datetime.datetime.now().time()
    date_today = datetime.datetime.today().date()

    if (time_now < MIN_TIME or time_now > MAX_TIME):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializer
    else:
        queryset = MenuHarian.objects.all().filter(tanggal=date_today) #return menu base on today
        serializer_class = MenuHarianSerializer

