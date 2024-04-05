from urllib.parse import urlencode
from django import template


register = template.Library()
@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name='get_encoded_dict')
def get_encoded_dict(data_dict):
    return urlencode(data_dict)