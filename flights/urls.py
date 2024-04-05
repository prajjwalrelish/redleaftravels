from django.urls import path
from . import views
from payment.views import flightPayment
urlpatterns = [
    path('search/',views.flightSearch,name='flight_search'),
    path('book/<int:id>/details',views.flightBookDetails,name='flight_book_details'),
    path('payment',flightPayment,name='flight_payment'),
]
