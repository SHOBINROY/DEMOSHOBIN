from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def calculation(request):

    return render(request,"home.html")
def home(request):
    return render(request,"calculation.html" ,)

def about(request):
    return render(request,"about.html")
def contacts(request):
    return render(request,"contacts.html")
def details(request):
    return render(request,"details.html")


def thanks(request):
    return HttpResponse("thank you")