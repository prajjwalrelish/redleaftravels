from celery import shared_task
from django.core.mail.message import EmailMessage
# from django.db.models.signals import pre_save
# from .models import Specialoffer
# from django.dispatch import receiver

@shared_task(bind = True)
def email_send(self,subject,message,to_email):
    email = EmailMessage(
        subject,message,to=[to_email]
    )
    email.send()
    return 'done'

# @shared_task(bind=True)
# @receiver(pre_save,sender=Specialoffer)
# def spo_active_false(sender,instance,**kwargs):
#     offers = Specialoffer.objects.filter(is_active = True)
#     for offer in offers:
#         print(offer)
#         offer.is_active = False 
#         offer.save()