import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flights.views import get_iata_code

# Create your views here.
@login_required(login_url='login')
def packagePayment(request): 
    if request.method == 'POST':
        uuid = request.POST['uuid']
        price = request.POST['price']
        package = request.POST['package']
        name = request.POST['name']
        email = request.POST['email']
        contact_number = request.POST['contact_number']
        date = request.POST['date']
        adults = request.POST['adults']
        children = request.POST['childrens']
        total_persons = int(adults) + int(children)
        amount = float(price) * total_persons

        details = {
            'type' : 'package',
            'package_uuid' : uuid,
            'name' : name,
            'package' : package,
            'email' : email,
            'contact_number' : contact_number,
            'date' : date,
            'adults' : adults,
            'childrens' : children,
            'amount' : amount,
        }
    return render(request,'payment.html',{'dict':json.dumps(details)})

@login_required(login_url='login')
def flightPayment(request):
    if request.method == 'POST' or request.method == 'GET':
        travelerDetails = {
            'type' : 'flight',
            'origin_code' :get_iata_code(request.GET['origin'] ),
            'destination_code' :get_iata_code( request.GET['destination'] ),
            'departure_date' : request.GET['departure_date'],
            'adults' : request.GET['adults'],
            'flight_id' : int(request.GET['id']),
            'fname' : request.POST['fname'],
            'lname' : request.POST['lname'],
            'email' : request.POST['email'],
            'number' : request.POST['number'],
            'birth_place' : request.POST['birth_place'],
            'gender' : request.POST['gender'],
            'dob' : request.POST['dob'],
            'passport_no' : request.POST['passport_no'],
            'passport_country' : request.POST['passport_country'],
            'passport_exp_date' : request.POST['passport_exp_date'],
            'passport_issue_date' : request.POST['passport_issue_date'],
            'amount':request.GET['amount']
        }

        # print(traveler_details['destination_code'],traveler_details['passport_no'])
       
        return render(request,'payment.html',{'travelerDetails':json.dumps(travelerDetails)})
