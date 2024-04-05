from django.shortcuts import render

from packeges.models import Package

# Create your views here.
def tour_search(request):
    if request.method == 'POST':
        from_place = request.POST['from']
        to_place = request.POST['to']
        tourPackages = Package.objects.filter(from_place=from_place,to_place=to_place)
        return render(request,'tours.html',{'tourPackages' : tourPackages})