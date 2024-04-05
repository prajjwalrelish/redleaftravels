from django.db import models
from django.db.models.fields.related import OneToOneField
import uuid
from packeges.models import Package
import datetime


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self) :
        return self.email

class Specialoffer(models.Model):
    package = OneToOneField(Package,on_delete=models.PROTECT)
    person = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    discount = models.IntegerField()
    desc = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     super(Specialoffer, self).save(*args, **kwargs)

    def __str__(self) :
        return f'{self.package.from_place} - {self.package.to_place}' 

class Blog(models.Model):
    default = uuid.uuid4
    uuid = models.UUIDField(default=default)
    author = models.CharField(max_length=50,default='divyanshu soni')
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to ='blogs/images',default='' )

    def __str__(self) :
        return self.title
    
class clientReview(models.Model):
    default = uuid.uuid4
    uuid = models.UUIDField(default=default)
    name = models.CharField(max_length=50)
    review = models.TextField()# 113 charcters
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to ='client_reviews/images',default='' )  
    date = models.DateField(default=datetime.date.today)

    def __str__(self) :
        return self.name
