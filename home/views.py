from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from .models import Subscriber,Contact,Specialoffer,Blog,clientReview

from packeges.models import Package
from django.views.decorators.csrf import csrf_exempt
# imports for amadeus flight boooking system
from amadeus import ResponseError 
from RedLeafTravels.settings import AMADEUS 

# to change the format of date for flight search api
import datetime

from .tasks import email_send
# Create your views here.

@csrf_exempt
def Home(request,from_place=None):
    # for displaying all packages info
    packages = Package.objects.all()
    # for displaying all special offers info
    specialoffer = Specialoffer.objects.order_by('-last_modified')[:1]
    # for displaying all blogs info
    blog = Blog.objects.all()
    # for displaying all client reviews
    clientreview = clientReview.objects.order_by('-date')[:3]
    
    # list of all from country in packages
    country_list = list(set(Package.objects.all().values_list('from_place', flat=True)))
    
    # to send list of all to country in packages when user clicks on a country
    if request.is_ajax and request.method =='POST':
        from_place =  request.POST['value']
        to_list = list(set(Package.objects.filter(from_place = from_place ).values_list('to_place',flat=True)))
        message = {
            'values' : to_list
        }
        return JsonResponse(message)
    return render(request, "index.html",{'packages':packages,'specialoffer':specialoffer,'blogs':blog,'clientreview':clientreview,'country_list': country_list})#,'to_list':to_list

def subscription(request):
 
    if request.is_ajax and request.method == "POST" : 
        message = {}
        email = request.POST['email']

        email_match = Subscriber.objects.filter(email = email)
        if email_match :
            message['message'] = f"The email '{email}' is already subscribed to us."
        else:
            instance = Subscriber(email= email)
            instance.save()
            message['message']='Congrats, You subscribed to Redleaf Travels'
            subject = 'Thanks for subscription.'
             # using celery function
            email_send.delay(subject,message['message'],email)

    return JsonResponse(message)       


def contactUs(request):
    if request.is_ajax and request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        message_match = Contact.objects.filter(message=message)
        message_dict = {
            'message':'we have got your message. we will try to reach you out as soon as possible.'
            }
        if not message_match:
            instance = Contact(name=name,email=email,message=message)
            instance.save()

        subject = 'we got the message.'
        # using celery function
        email_send.delay(subject,message_dict['message'],email)

        return JsonResponse(message_dict)
        
    return render(request,'contact_us.html')


def clientreview(request):
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        contact= request.POST['contact']
        image = request.FILES['image']
        review = request.POST['review']

        review = clientReview(name = name, email= email,address= address, contact= contact , review= review, image = image )
        review.save()
    return redirect('home')

def blogDetail(request,id):
    blog = Blog.objects.filter(uuid=id)
    return render(request,'blog/blog_detail.html' , {'blog':blog})

