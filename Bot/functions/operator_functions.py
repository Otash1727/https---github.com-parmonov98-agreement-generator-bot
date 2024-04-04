from shop.models import Operator,Refferral_link
from django.core.exceptions import ObjectDoesNotExist
from Bot.create_bot import bot
from Bot.keyboards import operator_kb
from aiogram.enums import ParseMode
from Bot.functions import customer_functions
from datetime import datetime

def operator_info():
    data=Operator.objects.all()
    if data!=None:
        return True
    else:
        return False

def add_reff_link(ref_link):
    fsm=Refferral_link(ref_link=ref_link)
    fsm.save()

def check_ref_link(ref_link):
    try:
        data=Refferral_link.objects.get(ref_link=ref_link)
        return True
    except ObjectDoesNotExist:
        return False
    
def add_operator(user_id,user_name):
    fsm=Operator(user_id=user_id,user_name=user_name)
    fsm.save()

def add_cont_count(user_id):
    fsm=Operator.objects.get(user_id=user_id)
    if fsm.contracts_count!=None:
        fsm.contracts_count+=1
        fsm.save()
    else:
        fsm.contracts_count=1
        fsm.save()

def check_operator(user_id):
    try:
        data=Operator.objects.get(user_id=user_id)
        return True
    except ObjectDoesNotExist:
        return False

def edit_name_operator(user_id,new_name):
    fsm=Operator.objects.get(user_id=user_id)
    fsm.user_name=new_name
    fsm.save()

def operator_TRUE():
    data=Operator.objects.filter(is_active=True)
    return data

def operator_FALSE():
    data=Operator.objects.filter(is_active=False)
    return data

def get_operator_all():
    data=Operator.objects.all()
    return data

def get_operator(user_id):
    data=Operator.objects.get(user_id=user_id)
    return data

def remove_opr(user_id):
    data=Operator.objects.get(user_id=user_id)
    data.delete()

def add_phone(user_id,phone):
    data=Operator.objects.get(user_id=user_id)
    data.phone_number=phone
    data.save()

def add_msg_id_opr(user_id,msg_id):
    data=Operator.objects.get(user_id=user_id)
    data.msg_id=msg_id
    data.save()

def add_msg_id2_opr(user_id,msg_id):
    fsm=Operator.objects.get(user_id=user_id)
    fsm.msg_id2=msg_id
    fsm.save()

def add_msg_id3_opr(user_id,msg_id):
    fsm=Operator.objects.get(user_id=user_id)
    fsm.msg_id3=msg_id
    fsm.save()

def add_msg_id4_opr(user_id,msg_id):
    fsm=Operator.objects.get(user_id=user_id)
    fsm.msg_id4=msg_id
    fsm.save()

def last_ID(user_id,last_id):
    fsm=Operator.objects.get(user_id=user_id)
    fsm.last_contract_id=last_id
    fsm.save()

def is_active_message(user_id,chat_id):
    get=get_operator(user_id=user_id)
    return  bot.send_message(chat_id=chat_id,text=f'<b>{get.user_name} sizda cheklovlar bor\nAdmin bilan bo\'g\'laning</b>',reply_markup=operator_kb.admin_inlin,parse_mode=ParseMode.HTML)

def fake_operator(chat_id,text):
    return  bot.send_message(chat_id=chat_id,text=f"{text}",reply_markup=operator_kb.remove)

def not_found_customer(chat_id):
    return bot.send_message(chat_id=chat_id,text="Mijoz topilmadi 🧐")     



async def auto_complate_callback(method_type,x_data):
    check_opr=check_operator(user_id=method_type)
    if check_opr==True:
        check_customer=customer_functions.check_customer(cont_id=x_data)
        get_opr=get_operator(user_id=method_type)
        if get_opr.is_active==True:
            if check_customer==True:
                data=customer_functions.get_customer(cont_id=x_data)
                mark_up=operator_kb.customer_info_edit(cont_id=x_data)
                msg_id= await bot.edit_message_text(chat_id=method_type,message_id=get_opr.msg_id,text=f"<b>Mijoz haqida umumiy ma'lumotlar\nShartnoma raqami - {data.pk}\nF.I.Sh - {data.full_name}\nYashash manzili - {data.place_of_residence}\nTelefon raqami - {data.phone_number}\nPasport seriysi - {data.passport_infos}\nPasportni berilgan vaqti - {data.date_of_issue}\nMahsulot nomi - {data.item_name}\nOldindan to'lov - {data.advance_payment}\nUmumiy qarzdorlik - {data.total_debt}\nMahsulotning umumiy narxi - {data.total_price}\nOylar soni - {data.months}\nOylik to'lov - {data.montly_payment}</b>",parse_mode=ParseMode.HTML,reply_markup=mark_up)
                add_msg_id_opr(user_id=method_type,msg_id=msg_id.message_id )
            else:
                await not_found_customer(chat_id=x_data)
        else:
            await is_active_message(user_id=method_type,chat_id=method_type)
    else:
        await fake_operator()
    

async def auto_complate_callback2(method_type,x_data):
    check_opr=check_operator(user_id=method_type)
    if check_opr==True:
        check_customer=customer_functions.check_customer(cont_id=x_data)
        get_opr=get_operator(user_id=method_type)
        if get_opr.is_active==True:
            if check_customer==True:
                data=customer_functions.get_customer(cont_id=x_data)
                mark_up=operator_kb.customer_info_edit(cont_id=x_data)
                msg_id= await bot.send_message(chat_id=method_type,text=f"<b>Mijoz haqida umumiy ma'lumotlar\nShartnoma raqami - {data.pk}\nF.I.Sh - {data.full_name}\nYashash manzili - {data.place_of_residence}\nTelefon raqami - {data.phone_number}\nPasport seriysi - {data.passport_infos}\nPasportni berilgan vaqti - {data.date_of_issue}\nMahsulot nomi - {data.item_name}\nOldindan to'lov - {data.advance_payment}\nUmumiy qarzdorlik - {data.total_debt}\nMahsulotning umumiy narxi - {data.total_price}\nOylar soni - {data.months}\nOylik to'lov - {data.montly_payment}</b>",parse_mode=ParseMode.HTML,reply_markup=mark_up)
                add_msg_id_opr(user_id=method_type,msg_id=msg_id.message_id )
            else:
                await not_found_customer(chat_id=x_data)
        else:
            await is_active_message(user_id=method_type,chat_id=method_type)
    else:
        await fake_operator()
    return msg_id.message_id

async def auto_complate_edit_info(cont_id,user_id,text,next_state):
    try:
        check_opr=check_operator(user_id=user_id)
        if check_opr==True:
            check_customer=customer_functions.check_customer(cont_id=cont_id)
            get_opr=get_operator(user_id=user_id)
            if get_opr.is_active==True:
                if check_customer==True:
                    markup=operator_kb.stop_state(cont_id=cont_id)
                    ms= await bot.send_message(chat_id=user_id,text=f"<b>{text}</b>",parse_mode=ParseMode.HTML,reply_markup=markup)
                    next_state
                    add_msg_id2_opr(user_id=user_id,msg_id=ms.message_id)
                else:
                    await not_found_customer(chat_id=user_id)
            else:
                await is_active_message(user_id=user_id,chat_id=user_id)
        else:
            await fake_operator() 
    except UnboundLocalError:
        pass




async def updates_data(cont_id,chat_id,msg_id):
    data=customer_functions.get_customer(cont_id=cont_id)
    message_reply_cus=customer_functions.customer_message_reply(cont_id=data.pk)
    message=await bot.edit_message_text(chat_id=chat_id,message_id=msg_id,text=f"<b>Mijoz haqida umumiy ma'lumotlar\nShartnoma raqami - {data.pk}\nF.I.Sh - {data.full_name}\nYashash manzili - {data.place_of_residence}\nTelefon raqami - {data.phone_number}\nPasport seriysi - {data.passport_infos}\nPasportni berilgan vaqti - {data.date_of_issue}\nMahsulot nomi - {data.item_name}\nOldindan to'lov - {data.advance_payment}\nUmumiy qarzdorlik - {data.total_debt}\nMahsulotning umumiy narxi - {data.total_price}\nOylar soni - {data.months}\nOylik to'lov - {data.montly_payment}</b>",reply_markup=message_reply_cus,parse_mode=ParseMode.HTML)
    return message
#shartnomani bekor qilishda knopklar chiqsin 

async def updates_data2(cont_id,chatID,msg_id):
    try:
        data2=customer_functions.get_customer(cont_id=cont_id)
        message_reply_cus=operator_kb.customer_info_edit(cont_id=cont_id)
        return  await bot.edit_message_text(chat_id=chatID,message_id=msg_id,text=f"<b>Mijoz haqida umumiy ma'lumotlar♻️\nShartnoma raqami - {data2.pk}\nF.I.Sh - {data2.full_name}\nYashash manzili - {data2.place_of_residence}\nTelefon raqami - {data2.phone_number}\nPasport seriysi - {data2.passport_infos}\nPasportni berilgan vaqti - {data2.date_of_issue}\nMahsulot nomi - {data2.item_name}\nOldindan to'lov - {data2.advance_payment}\nUmumiy qarzdorlik - {data2.total_debt}\nMahsulotning umumiy narxi - {data2.total_price}\nOylar soni - {data2.months}\nOylik to'lov - {data2.montly_payment}</b>",reply_markup=message_reply_cus,parse_mode=ParseMode.HTML)
    except:
        data2=customer_functions.get_customer(cont_id=cont_id)
        message_reply_cus=operator_kb.customer_info_edit(cont_id=cont_id)
        return  await bot.edit_message_text(chat_id=chatID,message_id=msg_id,text=f"<b>Mijoz haqida umumiy ma'lumotlar\nShartnoma raqami - {data2.pk}\nF.I.Sh - {data2.full_name}\nYashash manzili - {data2.place_of_residence}\nTelefon raqami - {data2.phone_number}\nPasport seriysi - {data2.passport_infos}\nPasportni berilgan vaqti - {data2.date_of_issue}\nMahsulot nomi - {data2.item_name}\nOldindan to'lov - {data2.advance_payment}\nUmumiy qarzdorlik - {data2.total_debt}\nMahsulotning umumiy narxi - {data2.total_price}\nOylar soni - {data2.months}\nOylik to'lov - {data2.montly_payment}</b>",reply_markup=message_reply_cus,parse_mode=ParseMode.HTML)


async  def ValueERROR_Func(msg_id,chat_id,message_opr_id,state_fsm,text,text2,Clear):
    check_opr=check_operator(user_id=chat_id)
    if check_opr==True:
        get_opr=get_operator(user_id=chat_id)
        if get_opr.is_active==True:
            msg_id=msg_id
            await bot.delete_message(chat_id=chat_id,message_id=message_opr_id)
            ms=await bot.send_message(chat_id=chat_id,reply_to_message_id=msg_id,text=f"<b>{text} raqamlarda ko'rsating\nFor example: {text2}</b>",parse_mode=ParseMode.HTML)
            state_fsm
            add_msg_id2_opr(user_id=chat_id,msg_id=ms.message_id)
            add_msg_id3_opr(user_id=chat_id,msg_id=msg_id)
        else:
            await is_active_message(user_id=chat_id,chat_id=chat_id)
            Clear
    else:
        await fake_operator(chat_id=chat_id,text=chat_id)
      

async def Edit_booln_Message(user_id,messageText,add_state,Get_state,current_msg_id,Clear,next_state,full_name,state_key,text2,func_name):
    check_opr=check_operator(user_id=user_id)
    if check_opr==True:
        get_oper=get_operator(user_id=user_id)
        if get_oper.is_active==True:
            try:
                text=int(messageText)
                add_state
                data= Get_state
                message_id=current_msg_id
                func_name(cont_id=get_oper.last_contract_id,text=data[state_key])
                Clear
                await bot.delete_messages(chat_id=user_id,message_ids=[message_id,get_oper.msg_id2])   
                await updates_data2(cont_id=get_oper.last_contract_id,chatID=user_id,msg_id=get_oper.msg_id)
            except ValueError:
                msd_id=get_oper.msg_id
                try:
                    await bot.delete_message(chat_id=user_id,message_id=get_oper.msg_id2)
                except:
                    pass
                markup=operator_kb.stop_state(cont_id=get_oper.last_contract_id)
                ms=await bot.send_message(chat_id=user_id,reply_to_message_id=msd_id,text=f"<b>{text2}</b>",parse_mode=ParseMode.HTML,reply_markup=markup)
                next_state
                add_msg_id2_opr(user_id=user_id,msg_id=ms.message_id)
                add_msg_id3_opr(user_id=user_id,msg_id=msd_id)
        else:
            await is_active_message(user_id=user_id,chat_id=user_id)
            Clear
    else:
        await fake_operator(chat_id=user_id,text=full_name)


def check_passport_expriy(passport_expriy_date):
    expriy_date=datetime.strptime(passport_expriy_date,'%d.%m.%Y')
    current_date=datetime.now()
    if expriy_date <=current_date:
        return True
    else:
        return False    
    

async def Wrong_message(chat_id,msid,current_msg_id,text,text2,next_state):
    await bot.edit_message_text(chat_id=chat_id,message_id=msid,text=f"<b>{text}</b>",parse_mode=ParseMode.HTML)
    msg_id=current_msg_id
    msg=await bot.send_message(chat_id=chat_id,text=f"<b>{text2}</b>",reply_to_message_id=msg_id,parse_mode=ParseMode.HTML,reply_markup=operator_kb.remove_state)
    next_state
    add_msg_id_opr(user_id=chat_id,msg_id=msg.message_id)    


async def Rigth_message(chat_id,msg_id,text,text2,add_state,next_state):
    await bot.edit_message_text(chat_id=chat_id,text=f"<b>{text}</b>",message_id=msg_id,parse_mode=ParseMode.HTML)
    msg=await bot.send_message(chat_id=chat_id,text=f"<b>{text2 }</b>",parse_mode=ParseMode.HTML,reply_markup=operator_kb.remove_state)
    add_state
    next_state
    add_msg_id_opr(user_id=chat_id,msg_id=msg.message_id)


async def Edit_Message(user_id,add_state,Get_state,current_msg_id,Clear,state_key,func_name):
    check_opr=check_operator(user_id=user_id)
    if check_opr==True:
        get_opr=get_operator(user_id=user_id)
        if get_opr.is_active==True:
            add_state
            data= Get_state
            message_id=current_msg_id
            print(data)
            func_name(cont_id=get_opr.last_contract_id,text=data[state_key])
            Clear
            try:
                await bot.delete_messages(chat_id=user_id,message_ids=[message_id,get_opr.msg_id2])   
            except :
                pass
            await updates_data2(cont_id=get_opr.last_contract_id,msg_id=get_opr.msg_id,chatID=user_id)
        else:
            await is_active_message(user_id=user_id,chat_id=user_id)
            Clear
    else:
        await fake_operator(chat_id=user_id,text=user_id)
       
