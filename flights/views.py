from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import datetime
import json
from .models import flightOrder
# imports for amadeus flight boooking system
from amadeus import ResponseError
from RedLeafTravels.settings import AMADEUS
# functions that coverts iatacode to city name nad city name to iata code
def get_airport_name(code):
    from csv import reader
    with open('IATA_codes.csv','r') as f :
        csv_reader = reader(f)
        for row in csv_reader: 
            if row[1] == code :
                return row[0]
def get_iata_code(name):
    from csv import reader
    with open('IATA_codes.csv','r') as f :
        csv_reader = reader(f)
        for row in csv_reader: 
            if row[0] == name :
                return row[1]


def dataExtractor(response):

    # number_of_bookable_seats = response['data'][0]['numberOfBookableSeats']
    # number_of_stops = response['data'][0]['itineraries'][0]['segments'][0]['numberOfStops']
    # number_of_stops_1 = response['data'][0]['itineraries'][0]['segments'][1]['numberOfStops']
    # currency = response['data'][0]['price']['currency']
    # ticket_price = response['data'][0]['travelerPricings'][0]['price']['total']

    no_of_offers = response['meta']['count']
    flight_details = []
    for offer in range(no_of_offers):
        flight = {}
        carrier_code = response['data'][offer]['itineraries'][0]['segments'][0]['carrierCode']
        flight['duration'] = response['data'][offer]['itineraries'][0]['duration']
        flight['carrier'] = response['dictionaries']['carriers'][carrier_code]
        flight['total_price'] = response['data'][offer]['price']['grandTotal']
        flight['id'] = int(response['data'][offer]['id']) - 1
        length_of_segments = len(response['data'][offer]['itineraries'][0]['segments'])
        info_list = []
        for i in range(length_of_segments):
            info_dict = {}
            info_dict['departure_iata_code'] =get_airport_name(  response['data'][offer]['itineraries'][0]['segments'][i]['departure']['iataCode'] )
            info_dict['departure_timing'] = response['data'][offer]['itineraries'][0]['segments'][i]['departure']['at']
            info_dict['arrival_iata_code'] =get_airport_name( response['data'][offer]['itineraries'][0]['segments'][i]['arrival']['iataCode'] )
            info_dict['arrival_timing'] = response['data'][offer]['itineraries'][0]['segments'][i]['arrival']['at']
            if i==(length_of_segments - 1):
                flight['arrival_timing'] = response['data'][offer]['itineraries'][0]['segments'][i]['arrival']['at']
            info_list.append(info_dict)
            flight['info'] = info_list
        flight_details.append(flight)
# format of flight data that is generated dynamically 
            # Dict =[ {
            #     'flight': {
            #         'duration': duration,
            #         'carrier': carrier,
            #         'total_price': total_price,
            #         'len_of_segments': length_of_segments,
            #         'info': [
            #             {
            #                 'departure_iata_code': departure_iata_code,
            #                 'departure_timing': departure_timing,
            #                 'arrival_iata_code': arrival_iatacode,
            #                 'arrival_timing': arrival_timing,
            #                 'no_of_stops': number_of_stops,
            #             },
            #             {
            #                 'departure_iata_code': departure_iata_code_1,
            #                 'departure_timing': departure_timing_1,
            #                 'arrival_iata_code': arrival_iatacode_1,
            #                 'arrival_timing': arrival_timing_1,
            #                 'no_of_stops': number_of_stops_1,
            #             }
            #         ]
            #         'arival_timing':'2021-12-24T10:55:00'
            #     }
            # }]

    return flight_details


def flightSearch(request):
    # response = AMADEUS.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2022-07-01', adults=2, max=4).result
    # return JsonResponse(response , safe=False)
    if request.method == "POST":
        origin = request.POST['origin']
        departure = request.POST['departure']
        adults = request.POST['adults']
        destination = request.POST['destination']
        # return_date = request.POST['return_date']
        childs = request.POST['childs']
        Class = request.POST['class']

        # ..................for flight offer search api the date format needs to be changed............
        # departure = datetime.datetime.strptime(input_date,'%m/%d/%Y').strftime('%Y-%m-%d')

        # parameters to send for the api as per documentation

        origin_code = get_iata_code(origin)
        destination_code = get_iata_code(destination)
        try:
            response = AMADEUS.shopping.flight_offers_search.get(originLocationCode=origin_code, destinationLocationCode=destination_code, departureDate=departure, adults=adults, max=4).result #'2022-06-01''yyyy-mm-dd'
           
            flightsData = dataExtractor(response)
            kwargs = {
                    'originLocation': origin,
                    'destinationLocation': destination,
                    'departueDate': departure,
                    'adults': adults,   
            }
           
            return render(request, 'flights/flight_offer.html', {'flights_data': flightsData,'kwargs':kwargs})

        except ResponseError as error:
            return HttpResponse('error', error)

@login_required(login_url='login')
def flightBookDetails(request,id):
    if request.method == 'GET' :   
        kwargs = {
            'origin' :request.GET.get('originLocation'),
            'destination' :request.GET.get('destinationLocation'),
            'departure_date' : request.GET.get('departueDate'),
            'adults' :  request.GET.get('adults'),
            'amount' :  request.GET.get('amount'),
            'id' : id
        }      
    return render(request,'flights/flight_book_details.html',{'kwargs' : kwargs})

# @login_required(login_url='login')
# def flightBook(request):
#     if request.method == 'POST' or request.method == 'GET':
#         traveler_details = {
#             'origin_code' :get_iata_code(request.GET['origin'] ),
#             'destination_code' :get_iata_code( request.GET['destination'] ),
#             'departure_date' : request.GET['departure_date'],
#             'adults' : request.GET['adults'],
#             'flight_id' : int(request.GET['id']),
#             'fname' : request.POST['fname'],
#             'lname' : request.POST['lname'],
#             'email' : request.POST['email'],
#             'number' : request.POST['number'],
#             'birth_place' : request.POST['birth_place'],
#             'gender' : request.POST['gender'],
#             'dob' : request.POST['dob'],
#             'passport_no' : request.POST['passport_no'],
#             'passport_country' : request.POST['passport_country'],
#             'passport_exp_date' : request.POST['passport_exp_date'],
#             'passport_issue_date' : request.POST['passport_issue_date'],

#         }
#         details = {
#                 'type' : 'flight',
#                 'amount':request.GET['amount']
#         }
#         return render(request,'payment.html',{'dict':json.dumps(details),'traveler_details':traveler_details})

     

def flight_order(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        transacion_id =  body["transaction_id"]
        amount =  body["amount"]
        origin_code = body['origin_code'] 
        destination_code = body['destination_code'] 
        departure_date = body['departure_date']
        adults = body['adults']
        flight_id = body['flight_id']
        fname = body['fname']
        lname =  body['lname']
        email = body['email']
        number = body['number']
        birth_place= body['birth_place']
        gender = body['gender']
        dob = body['dob']
        passport_no = body['passport_no']
        passport_country = body['passport_country']
        passport_exp_date = body['passport_exp_date']
        passport_issue_date = body['passport_issue_date']



        print(f'{origin_code},{destination_code},{transacion_id},{amount}')

        
        flights = AMADEUS.shopping.flight_offers_search.get(originLocationCode=origin_code, destinationLocationCode=destination_code, departureDate=departure_date, adults=adults, max=3).data

        # flights[0]['price']['total'] = '500'

        price_confrim = AMADEUS.shopping.flight_offers.pricing.post(flights[flight_id]).result

        try:
            if price_confrim['warnings']:
                return JsonResponse(price_confrim['warnings'][0]['detail'], safe=False)
        except :
            # raise error
            traveler = {
                'id': '1',
                'dateOfBirth': dob,
                'name': {
                    'firstName': fname,
                    'lastName': lname
                },
                'gender': gender,
                'contact': {
                    'emailAddress': email,
                    'phones': [{
                        'deviceType': 'MOBILE',
                        'countryCallingCode': '91',
                        'number': number
                    }]
                },
                'documents': [{
                    'documentType': 'PASSPORT',
                    'birthPlace': birth_place,
                    'issuanceLocation': birth_place,
                    'issuanceDate': passport_issue_date,
                    'number': passport_no,
                    'expiryDate': passport_exp_date,
                    'issuanceCountry': passport_country,
                    'validityCountry': passport_country,
                    'nationality':passport_country,
                    'holder': True
                }]
            }
            
            # Flight Create Orders to book the flight

            booked_flight = AMADEUS.booking.flight_orders.post(flights[flight_id], traveler).result
            flight_book_id = booked_flight['data']['id']
            # print(booked_flight['data']['flightOffers'][0]['price']['grandTotal'])
            # ......................get flight orders by order id..............
            # response = AMADEUS.booking.flight_order(booked_flight['data']['id']).get()
            # ................delete flight orders by order id.............
            # response = AMADEUS.booking.flight_order(booked_flight['data']['id']).delete()
            # print(response.result)
            # return JsonResponse(booked_flight,safe=False)
            order = flightOrder(book_id = flight_book_id, transaction_id = transacion_id,price=amount)
            order.save()

            return HttpResponse('payment success')



