from django.urls import path
from . import views
urlpatterns = [
    path('search/',views.tour_search, name='tour_search'),
]
