from django.urls import path
from packeges import views
urlpatterns = [
    path('detail/<uuid:id>/',views.packageDetail,name='package_detail'),
    path('book/<uuid:id>/',views.packageBook,name='package_detail'),
]
