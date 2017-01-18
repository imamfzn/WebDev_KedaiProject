from django.conf.urls import url,include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import *

router = routers.DefaultRouter()
#cust_router = routers.DefaultRouter()

router.register(r'pelanggan', Pelanggan,base_name='pelanggan')
router.register(r'pesanan_pelanggan', PesananPelanggan,base_name='pesanan_pelanggan')
router.register(r'gedung', GedungViewSet,base_name='gedung')
router.register(r'pesanan', PesananViewSet,base_name='pesanan')
router.register(r'pesanancust', PesananCustViewSet,base_name='pesanancust')
router.register(r'suplier', SuplierViewSet)
router.register(r'menu', MenuViewSet,base_name='menu')
router.register(r'menuharian', MenuHarianViewSet,base_name='menuharian')
router.register(r'menucust',MenuPelangganViewSet,base_name='menucust')
#router.register(r'menutest',MenuHarianTest,base_name='menutest')

swaggerdocs = get_swagger_view(title='Kedai API')

urlpatterns = [
	url(r'^pelanggan/(?P<pk>[0-9]+)/pesanan/$', PesananPelanggan),
    url(r'^servertime/', ServerTime.as_view()),
    url(r'^docs/',swaggerdocs),
    url(r'^menutest',MenuHarianList.as_view())
]

urlpatterns += router.urls
