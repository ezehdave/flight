from . import views
from django.urls import path
urlpatterns =[
    path("", views.index, name='home'),
    path("login", views.loginpage, name='login'),
    path('logout/', views.logoutpage, name="logout"),

    path("register", views.registerpage, name='register'),

    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("ship_a_parcel", views.shipParcel, name='ship_a_parcel'),
    path("track_a_parcel", views.trackParcel, name='track_a_parcel'),
    path("services", views.service, name='services'),
    path("faqs", views.faqs, name='faqs'),
    path("make_payment", views.crytoDeposit, name='make_payment'),
    path("404_error", views.error, name='404_error'),

]
