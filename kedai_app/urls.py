from django.conf.urls import url,include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import *

router = routers.DefaultRouter()
router.register(r'pelanggan', PelangganViewSet)
router.register(r'gedung', GedungViewSet)
router.register(r'pesanan', PesananViewSet)
#router.register(r'pesanan_customer', PesananCustomerViewSet,base_name='pesanan_customer')
router.register(r'suplier', SuplierViewSet)
router.register(r'menu', MenuViewSet)
#router.register(r'menucustomer', MenuCustomerViewSet)
router.register(r'menuharian', MenuHarianViewSet)
router.register(r'menupelanggan',MenuPelangganViewSet,base_name='menu_pelanggan')

swaggerdocs = get_swagger_view(title='Kedai API')

urlpatterns = [
    url(r'^servertime/', ServerTime.as_view()),
    url(r'^docs/',swaggerdocs)
]


urlpatterns += router.urls