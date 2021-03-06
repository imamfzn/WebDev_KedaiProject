from rest_framework import viewsets,generics
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
    permission_classes = [CustPostPermission]
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
        id_menus = MenuHarian.objects.all().filter(tanggal = date_today).values('menu')
        queryset = Menu.objects.all().filter(id_menu__in = id_menus)
        serializer_class = MenuSerializer

class MenuHarianList(generics.GenericAPIView):
    queryset = MenuHarian.objects.all()
    serializer_class = MenuTest

    def get(self, request):
        queryset = MenuHarian.objects.all()
        serializer = MenuTest(queryset,many=True)
        return Response(serializer.data)

    def post(self, request):
        menu = Menu.objects.get(id_menu = request.data.get('menu'))
        #print(request.data.get('id_menu'))
        serializer = MenuTest(menu,data=request.data)
        if serializer.is_valid():
            serializer.save(
                menu = menu,
                tanggal = datetime.datetime.now().date())
            return Response(serializer.data)


class PesananPelangganViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyCustomerService]
    queryset = Pelanggan.objects.all()
    serializer_class = PesananPelanggan

class PesananPelanggan(generics.GenericAPIView):
    def get(self, request, pk):
        try:
            pelanggan = Pelanggan.objects.filter(id_pelanggan=int(pk))
            queryset = pelanggan

        except ObjectDoesNotExist:
            return Response(
                {"detail": "Not found."})

        serializer = PesananPelanggan(pelanggan)
        print(serializer.data)
        return Response(serializer.data)




    

