from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'home.html')




    
 









def about(request):
    return render(request,'about.html')

 
def services1(request):
 return HttpResponse("this is services1 page")



 
def signup(request):
    return render(request,'signup.html')



def contact(request):
    return render(request,'contact.html')



def appointment(request):
    return render(request,'appointment.html')