from django.conf.urls import url,include
from rest_framework import routers
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

urlpatterns = [
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^servertime/', ServerTime.as_view()),
]


urlpatterns += router.urls