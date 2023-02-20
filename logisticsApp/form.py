from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Ship_booking, Contact_us


class signUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': "",
            'placeholder': "Username",
            'class': "email",
            'name': "username",
        })
        self.fields['email'].widget.attrs.update({
            'required': "",
            'placeholder': "email",
            'class': "email",
            'name': "email",
        })
        self.fields['password1'].widget.attrs.update({
            'required': "",
            'placeholder': "password",
            'class': "email",
            'name': "password",
        })
        self.fields['password2'].widget.attrs.update({
            'required': "",
            'placeholder': " confirm-password",
            'class': "email",
            'name': "confirm-password",
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Contact_usForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'required': "",
            'placeholder': "type your name ",
            'name': "name",
        })
        self.fields['email'].widget.attrs.update({
            'required': "",
            'placeholder': "type your email ",
            'name': "name",
        })
        self.fields['phone_no'].widget.attrs.update({
            'required': "",
            'placeholder': "type your phone_no ",
            'name': "name",
        })
        self.fields['subject'].widget.attrs.update({
            'required': "",
            'placeholder': "massage subject  ",
            'name': "name",
        })
        self.fields['massage'].widget.attrs.update({
            'required': "",
            'cols': "30",
            "rows": "10",
            'placeholder': " type your massage   ",
            'name': "name",
        })

    class Meta:
        model = Contact_us
        fields = "__all__"




class Ship_bookingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['senders_name'].widget.attrs.update({
            'required': "",
            'placeholder': "senders_name",
            'name': "name",
        })
        self.fields['senders_email'].widget.attrs.update({
            'required': "",
            'placeholder': "senders_email",
            'name': "email",
        })
        self.fields['senders_phone_no'].widget.attrs.update({
            'required': "",
            'placeholder': "senders_phone_no",
            'name': "email",
        })
        self.fields['senders_address'].widget.attrs.update({
            'required': "",
            'placeholder': "senders_address",
            'name': "email",
        })
        self.fields['receivers_name'].widget.attrs.update({
            'required': "",
            'placeholder': "receivers_name",
            'name': "email",
        })
        self.fields['receivers_email'].widget.attrs.update({
            'required': "",
            'placeholder': "receivers_email",
            'name': "email",
        })
        self.fields['receivers_phone_no'].widget.attrs.update({
            'required': "",
            'placeholder': "receivers_phone_no",
            'name': "email",
        })
        self.fields['receivers_address'].widget.attrs.update({
            'required': "",
            'placeholder': "receivers_address",
            'name': "email",
        })
        self.fields['receivers_Zip_code'].widget.attrs.update({
            'required': "",
            'placeholder': "receivers_Zip_code",
            'name': "email",
        })
        self.fields['Estimated_parcels_weight'].widget.attrs.update({
            'required': "",
            'placeholder': "Estimated_parcels_weight",
            'name': "email",
        })
        self.fields['massage'].widget.attrs.update({
            'required': "",
            'cols':"30",
            "rows":"10",
            'placeholder': "massage",
            'name': "email",
        })

    class Meta:
        model = Ship_booking
        fields = "__all__"
        exclude = ["tracking_id","created_on"]



