from django.db import models
from django.db.models.fields.related import OneToOneField
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Package(models.Model):
    default = uuid.uuid4
    rating = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )

    uuid = models.UUIDField(default=default)
    from_place = models.CharField(max_length=300)
    to_place = models.CharField(max_length=300 )
    image = models.ImageField(default='',upload_to='packages/images')
    price = models.CharField(max_length=15)
    accomodation = models.IntegerField(default=5)
    no_of_days = models.IntegerField()
    no_of_nights = models.IntegerField(default=5)
    transportation = ArrayField(models.CharField(max_length=50),default=None)
    food_facilities = ArrayField(models.CharField(max_length=50),default=None)
    rating = models.IntegerField(choices=rating)
    reviews = models.CharField(max_length=500,null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.from_place} - {self.to_place} '


class order_package(models.Model):
    default = uuid.uuid4
    uuid = models.UUIDField(default=default,primary_key=True)
    order_id = models.CharField(max_length=300,default='') 
    package_uuid = models.UUIDField(default=default)
    package = OneToOneField(Package,on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=14)
    email = models.EmailField()
    package_date = models.CharField(max_length=11)
    adults = models.IntegerField()
    childrens = models.IntegerField()
    paid_amount = models.CharField(max_length=50 , default='200')
