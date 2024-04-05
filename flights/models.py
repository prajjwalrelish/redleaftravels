from django.db import models
import uuid
from django.utils import timezone
# Create your models here.
class flightOrder(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True)
    book_id = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    date = models.DateTimeField(editable=True,auto_now=True)