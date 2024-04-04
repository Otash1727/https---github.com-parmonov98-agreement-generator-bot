from shop.models import Creator
from django.core.exceptions import ObjectDoesNotExist
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Bot.functions.operator_functions import * 
def check_creator(user_id):
    try:
        data=Creator.objects.get(user_id=user_id)
        return True
    except ObjectDoesNotExist:
        return False    
def add_username_admin(user_id,Username):
    data=Creator.objects.get(user_id=user_id)
    data.username=Username
    data.save()

def get_creator_all():
    data=Creator.objects.all()
    return data 

def add_msg_id2(user_id,msg_id):
    data=Creator.objects.get(user_id=user_id)
    data.msg_id2=msg_id
    data.save()   

def add_msg(msg_id,user_id):
    data=Creator.objects.get(user_id=user_id)
    data.msg_id=msg_id
    data.save()

def get_msg_id(user_id):
    try:
        data=Creator.objects.get(user_id=user_id)
        return data.msg_id
    except ObjectDoesNotExist:
        pass


def message_reply():
    get_operator=get_operator_all()
    markup_btn=InlineKeyboardBuilder()
    for i in get_operator:
        markup_btn.row(InlineKeyboardButton(text=f"{i.user_name}",callback_data=f"users {i.user_id}"),width=2)
    return  markup_btn.as_markup()


def add_last_botton(user_id,last_button_text):
    data=Creator.objects.get(user_id=user_id)
    data.last_button_text=last_button_text
    data.save()

def get_info_creator(user_id):
    data=Creator.objects.get(user_id=user_id)
    return data

def op_is_active(opr_id):
    fsm=Operator.objects.get(user_id=opr_id)
    if fsm.is_active==True:
        fsm.is_active=False
        fsm.save()
    else:
        fsm.is_active=True
        fsm.save()
    return print(fsm.user_name)

def last_opr_ID(user_id,lastID):
    data=Creator.objects.get(user_id=user_id)
    data.last_opr_id=lastID
    data.save()

def get_creator(user_id):
    data=Creator.objects.get(user_id=user_id)
    return data 
