from django.contrib import admin
from .models import Operator,Customer,Creator,Refferral_link


class OperatorAdmin(admin.ModelAdmin):
    model=Operator
    list_display=Operator.List_display


class CustomerAdmin(admin.ModelAdmin):
    model=Customer
    list_display=Customer.ListDisplay

class CreatorAdmin(admin.ModelAdmin):
    list_display=['user_name','user_id']

class Referral_linkAdmin(admin.ModelAdmin):
    list_display=['ref_link']

admin.site.register(Operator,OperatorAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Creator,CreatorAdmin)
admin.site.register(Refferral_link,Referral_linkAdmin)

