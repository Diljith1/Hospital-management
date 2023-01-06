from django.shortcuts import render
from .models import Department,Doctor
from .forms import Bookingform

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def doctors(request):
    dict_doc={
        'doc':Doctor.objects.all()
    }
    return render(request,'doctors.html',dict_doc)

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)

def booking(request):
    if request.method=="POST":
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()

            return render(request,'confirmation.html')
    formvb=Bookingform()
    dict_book={
        'book':formvb
    }
    return render(request,'booking.html',dict_book)