from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .models import Package,order_package

def packageDetail(request,id):
    package = Package.objects.filter(uuid=id)
    return render(request,'packages/package_detail.html',{'package':package})

@login_required(login_url='login')
def packageBook(request,id):
    package = Package.objects.get(uuid=id)
    print(package)
    return render(request,'packages/package_book.html',{'package' : package})

def packageOrder(request): 
    if request.method == 'POST':
        body = json.loads(request.body)
        transacion_id =  body["transaction_id"]
        package_uuid =  body["package_uuid"]
        amount =  body["amount"]
        name =  body["name"]
        email =  body["email"]
        contact_number =  body["contact_number"]
        date =  body["date"]
        adults =  body["adults"]
        childrens =  body["childrens"]
        
        package = Package.objects.get(uuid=package_uuid)

        order = order_package(order_id = transacion_id ,package=package,package_uuid = package_uuid , name = name, contact_no = contact_number, email = email,  package_date = date,adults = adults,childrens = childrens,paid_amount = amount)
        order.save() 
       
        return HttpResponse('payment success')
