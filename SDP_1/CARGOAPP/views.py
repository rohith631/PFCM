from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mad(request):
    return render(request,'CARGOAPP/home.html')
def mad1(request):
    return render(request,'CARGOAPP/adminpage.html')
def mad2(request):
    return render(request,'CARGOAPP/transactions.html')
def mad3(request):
    return render(request,'CARGOAPP/tracking.html')
def mad4(request):
    return render(request,'CARGOAPP/shipping.html')
def mad5(request):
    return render(request,'CARGOAPP/order.html')
def mad6(request):
    return render(request,'CARGOAPP/new to speedo.html')
def mad7(request):
    return render(request,'CARGOAPP/delivery.html')




