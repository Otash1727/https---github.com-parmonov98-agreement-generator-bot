from shop.models import Customer
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,CallbackQuery
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q



def add_customer(full_name,place_of_residence,phone_number,passport_infos,date_of_issue,item_name,advance_payment,total_debt,total_price,montly_payment,month,which_operator,operator_id):
    fms=Customer.objects.create(full_name=full_name,place_of_residence=place_of_residence,phone_number=phone_number,passport_infos=passport_infos,date_of_issue=date_of_issue,item_name=item_name,advance_payment=advance_payment,total_debt=total_debt,total_price=total_price,montly_payment=montly_payment,months=month,which_operator=which_operator,operator_id=operator_id)
    return fms.contract_number



def customer_message_reply(cont_id):
    get_customer=Customer.objects.filter(contract_number=cont_id)
    markup_btn=InlineKeyboardBuilder()
    for i in get_customer:
        markup_btn.row(InlineKeyboardButton(text="Ma'lumotlarni tahrirlash",callback_data=f"info {i.contract_number}")).row(InlineKeyboardButton(text="PDF yuklash 📥 ",callback_data=f"pdf {i.contract_number}"))
    return markup_btn.as_markup()

def customer_message_reply2(cont_id):
    get_customer=Customer.objects.filter(contract_number=cont_id)
    markup_btn=InlineKeyboardBuilder()
    for i in get_customer:
        markup_btn.row(InlineKeyboardButton(text="Ma'lumotlarni tahrirlash",callback_data=f"info2 {i.contract_number}")).row(InlineKeyboardButton(text="PDF yuklash 📥 ",callback_data=f"pdf2 {i.contract_number}"))
    return markup_btn.as_markup()
   

def get_customer_all():
    data=Customer.objects.all()
    return data

def check_customer(cont_id):
    try:
        Customer.objects.get(contract_number=cont_id)
        return True
    except ObjectDoesNotExist:
        return False


def get_customer(cont_id):
    data=Customer.objects.get(contract_number=cont_id)
    return data

def add_file_Id(dd,cont_id):
    try:
        fsm=Customer.objects.get(contract_number=cont_id)
        fsm.File_ID=dd
        fsm.save()
    except ObjectDoesNotExist:
        pass


def auto_complate(method_type,description,model_info,):
    return method_type(text=f"Mijozning {description} o'zgartirishni xoxlaysizmi",show_alert=True)

def edit_fullname(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.full_name=text
    fsm.save()


def edit_place(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.place_of_residence=text
    fsm.save()

def edit_phone(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.phone_number=text
    fsm.save()


def edit_paspord(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.passport_infos=text
    fsm.save()

def edit_paspord_date(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.date_of_issue=text
    fsm.save()


def edit_item(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.item_name=text
    fsm.save()

def edit_total_price(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.total_price=text
    fsm.save()

def edit_advanced_pay(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.advance_payment=text
    fsm.save()

def edit_total_debt(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.total_debt=text
    fsm.save()

def edit_monthly_pay(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.montly_payment=text
    fsm.save()


def edit_month(cont_id,text):
    fsm=Customer.objects.get(contract_number=cont_id)
    fsm.months=text
    fsm.save()

def get_customer_WhichOpr(opr_id):
    data=Customer.objects.filter(operator_id=opr_id)
    return data


def search_customer(query, oper_id):
    try:
        split_query = query.query.split("search#")
        if len(split_query) < 2:
            return Customer.objects.none()

        search_term = split_query[1].strip()
        search_filter = (
            Q(full_name__startswith=search_term, operator_id=oper_id) |
            Q(place_of_residence__startswith=search_term, operator_id=oper_id) |
            Q(phone_number__startswith=search_term, operator_id=oper_id) |
            Q(passport_infos__startswith=search_term, operator_id=oper_id) |
            Q(date_of_issue__startswith=search_term, operator_id=oper_id) |
            Q(item_name__startswith=search_term, operator_id=oper_id) |
            Q(contract_number__startswith=search_term, operator_id=oper_id) |
            Q(advance_payment__startswith=search_term, operator_id=oper_id) |
            Q(total_debt__startswith=search_term, operator_id=oper_id) |
            Q(total_price__startswith=search_term, operator_id=oper_id) |
            Q(montly_payment__startswith=search_term, operator_id=oper_id) |
            Q(months__startswith=search_term, operator_id=oper_id)
        )
        data = Customer.objects.filter(search_filter)
        return data
    except (ObjectDoesNotExist, UnboundLocalError):
        print('not found')
        return Customer.objects.none()

def search_customer_byAdmin(query):
    try:
        split_query = query.query.split("customers")
        if len(split_query) < 2:
            return Customer.objects.none()

        search_term = split_query[1].strip()
        search_filter = (
            Q(full_name__startswith=search_term) |
            Q(place_of_residence__startswith=search_term) |
            Q(phone_number__startswith=search_term) |
            Q(passport_infos__startswith=search_term) |
            Q(date_of_issue__startswith=search_term) |
            Q(item_name__startswith=search_term) |
            Q(contract_number__startswith=search_term) |
            Q(advance_payment__startswith=search_term) |
            Q(total_debt__startswith=search_term) |
            Q(total_price__startswith=search_term) |
            Q(montly_payment__startswith=search_term) |
            Q(months__startswith=search_term)
        )
        data = Customer.objects.filter(search_filter)
        return data
    except (ObjectDoesNotExist, UnboundLocalError):
        print('not found')
        return Customer.objects.none()