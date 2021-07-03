from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    
     return render(request,'site.html')
    #return HttpResponse("this is home page")
def homm(request):
    #return HttpResponse("this is home page")
    return render(request,'homm.html')
def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html')
def services(request):
    #return HttpResponse("this is services")
    return render(request,'services.html')      

def contact(request):
    #return HttpResponse("this is contact")    
    return render(request,'contact.html')