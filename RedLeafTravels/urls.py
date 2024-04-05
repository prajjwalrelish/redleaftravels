"""RedLeafTravels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.urls.conf import include 
from home.views import Home,subscription,contactUs,clientreview,blogDetail



from packeges import urls as packages_urls
from usermgmt import urls as usermgmt_urls
from payment import urls as payment_urls
from tours import urls as tours_urls
from flights import urls as flights_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name="home"),
    
    path('payment/',include(payment_urls)),
    path('packages/',include(packages_urls)),
    path('user/',include(usermgmt_urls)),
    path('tours/',include(tours_urls)),
    path('flights/',include(flights_urls)),
   

    path('subscribe',subscription,name='subscribe'),
    path("contact-us", contactUs , name="contact_us"),  
    path('client-review',clientreview,name='client_review'),
    path('blog-detail/<uuid:id>',blogDetail, name='blog_detail'),
 

]

# for handling media(images) files
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
