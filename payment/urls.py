from django.urls import path

from .views import packagePayment
from packeges.views import packageOrder
from flights.views import flight_order

urlpatterns = [
    path('package',packagePayment,name='package_payment'),
    path('package/done',packageOrder,name='package_payment_done'),
    path('flight/done',flight_order,name='flight_payment_done')
]
