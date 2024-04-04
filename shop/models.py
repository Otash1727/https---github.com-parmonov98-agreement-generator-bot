from django.db import models
from django.utils import timezone




class Creator(models.Model):
    user_name=models.CharField(max_length=50)
    user_id=models.IntegerField()
    bot_id=models.IntegerField(null=True,blank=True)
    last_button_text=models.CharField(max_length=50,null=True,blank=True)
    msg_id=models.IntegerField(null=True,blank=True)
    msg_id2=models.IntegerField(null=True,blank=True)
    msg_id3=models.IntegerField(null=True,blank=True)
    last_opr_id=models.IntegerField(null=True,blank=True)
    crteated_at=models.DateTimeField(default=timezone.now)



class Operator(models.Model):
    user_name=models.CharField(max_length=100,null=True,blank=True)
    user_id=models.IntegerField()
    phone_number=models.CharField(max_length=13,null=True,blank=True)
    contracts_count=models.IntegerField(null=True,blank=True)
    msg_id=models.IntegerField(null=True,blank=True)
    msg_id2=models.IntegerField(null=True,blank=True)
    msg_id3=models.IntegerField(null=True,blank=True)
    msg_id4=models.IntegerField(null=True,blank=True)
    last_contract_id=models.IntegerField(null=True,blank=True)
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=timezone.now)
    List_display=['user_name','phone_number','contracts_count','created_at']

class Refferral_link(models.Model):
    ref_link=models.CharField(max_length=16,null=True,blank=True)
    created_at=models.DateTimeField(default=timezone.now)

class Customer(models.Model):
    full_name=models.CharField(max_length=100)
    place_of_residence=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=13,null=True,blank=True)
    passport_infos=models.CharField(max_length=50)
    date_of_issue=models.CharField(max_length=50)
    item_name=models.CharField(max_length=150)
    contract_number=models.AutoField(primary_key=True)
    advance_payment=models.IntegerField()
    total_debt=models.IntegerField()
    total_price=models.IntegerField()
    montly_payment=models.IntegerField()
    months=models.IntegerField()
    File_ID=models.CharField(max_length=300,null=True,blank=True)
    which_operator=models.CharField(max_length=100)
    operator_id=models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now)
    ListDisplay=['contract_number','full_name','phone_number','total_debt','which_operator']


#admin callback x lambda 