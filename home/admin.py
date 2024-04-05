from django.contrib import admin
from .models import Contact, Subscriber,Specialoffer,Blog,clientReview
# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Contact)
admin.site.register(Specialoffer)
admin.site.register(Blog)
admin.site.register(clientReview)
