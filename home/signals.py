from django.db.models.signals import post_save, pre_save
from home.models import Specialoffer
from django.dispatch import receiver


# @receiver(pre_save,sender=Specialoffer)
# def specialoffer_active_false(sender,instance,**kwargs):
#     offers = Specialoffer.objects.filter(is_active = True)
#     for offer in offers:
#         # print(offer)
#         offer.is_active = False 
        # offer.save()