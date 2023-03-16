from django.db import models
from django.contrib.auth.models import User
class Crypto_Payment_detail(models.Model,):
    admin_name= models.CharField(max_length=250)
    btc_coin = models.CharField(max_length=250)
    ETH_coin = models.CharField(max_length=250)
    BNB_coin = models.CharField(max_length=250)
    USDT_coin = models.CharField(max_length=250)


    def __str__(self):
        return self.admin_name




class Contact_us(models.Model, ):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_no = models.CharField(blank=True, null=True, max_length=250)
    subject = models.CharField(max_length=250)
    massage = models.TextField(blank=True, null=True, )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name


class Ship_booking(models.Model):
    senders_name = models.CharField(max_length=250,)
    senders_email = models.CharField(max_length=250)
    senders_phone_no = models.CharField( null="null", max_length=250)
    senders_address = models.CharField(max_length=250)
    receivers_name = models.CharField(max_length=250)
    receivers_email = models.CharField(max_length=250)
    receivers_phone_no = models.CharField(blank=True, null=True, max_length=250 )
    receivers_address = models.CharField(max_length=250)
    receivers_Zip_code = models.CharField(max_length=250)
    Estimated_parcels_weight = models.CharField(max_length=250)
    massage = models.TextField(blank=True, null=True)
    tracking_id = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, null=True, blank=False)



    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.senders_name
class Delivery_destination(models.Model):
    tracking_id = models.ForeignKey(Ship_booking, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    delivery_status = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ["-location"]