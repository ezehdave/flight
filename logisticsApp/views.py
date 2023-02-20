from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.contrib import messages
from .form import signUpForm
import datetime
from .form import *


# Create your views here.

def loginpage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "password does not exist")

    context = {'page': page}
    return render(request, 'login_register.html', context)

def logoutpage(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    form = signUpForm()
    if request.method == "POST":
       form = signUpForm(request.POST)
       if form.is_valid():
            user = form.save(commit=False)
            user.email= user.email.lower()
            user.save()
            login(request, user)
            return redirect("home")
       else:
           messages.error(request, "an error occured during registration")

    context = {'form':form}
    return render(request,'login_register.html', context)


def index(request):
    context = {}
    return render(request, 'index.html', context)


def contact(request):
    form = Contact_usForm()
    if request.method == "POST":
        form = Contact_usForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "form submitted successfully")
            return redirect("contact")
    context = {"form": form}
    return render(request, 'contact.html', context)

def shipParcel(request):
    form = Ship_bookingForm()
    tracking_no = datetime.datetime.now().timestamp()
    form = Ship_bookingForm()
    if request.method == "POST":
       form = Ship_bookingForm(request.POST)
       if form.is_valid():
           contact_form = form.save(commit=False)
           contact_form.tracking_id = tracking_no
           contact_form.save()
           messages.success(request, "Form submitted successfully, we will get back to you via you mail")
           return redirect("ship_a_parcel")
    context = { "form":form }
    return render(request, 'ship-a-parcel.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)



def trackParcel(request):
    results=""
    if request.method == "POST":
        track_id = request.POST.get('tracking_id')


        try:
            results = Ship_booking.objects.get(tracking_id=track_id)
            if results.status == False:
                results.status ="pending"
            else:
                results.status = "processed"


        except:
            messages.error(request, "Tracking Id does not exist")

    context = {"results":results}
    return render(request, 'track-a-parcel.html', context)

def service(request):
    context = {}
    return render(request, 'service.html', context)

def faqs(request):
    form = Contact_usForm()
    if request.method == "POST":
        form = Contact_usForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "form submitted successfully")
            return redirect("faqs")
    context = {"form": form}
    return render(request, 'faqs.html', context)