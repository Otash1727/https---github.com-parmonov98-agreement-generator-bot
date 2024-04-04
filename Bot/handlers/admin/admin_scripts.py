from Bot.create_bot import bot,dp 
from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Bot.functions import operator_functions,admin_functions,customer_functions
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from Bot.config import BOT_NICKNAME
from Bot.keyboards import admin_kb
from Bot.inline_query import inlines
import secrets,time  


router=Router()


class Name(StatesGroup):
    name=State()
    





@router.message(F.text=='Foydalanuvchilar')
async def client_info(message:Message):
    check_creator=admin_functions.check_creator(user_id=message.from_user.id)
    if check_creator==True:
        operator_info=operator_functions.operator_info()
        admin_functions.add_last_botton(user_id=message.from_user.id,last_button_text=message.text)
        if operator_info==True:
            message_reply=admin_functions.message_reply()
            msg_id=await bot.send_message(chat_id=message.from_user.id,text='Operatorlar ro\'yhati',reply_markup=message_reply)       
            get_msg_id=admin_functions.get_msg_id(user_id=message.from_user.id)
            try:
                await bot.delete_message(chat_id=message.from_user.id,message_id=get_msg_id)
            except:
                pass
            admin_functions.add_msg(msg_id=msg_id.message_id,user_id=message.from_user.id)
        else:
            pass
    else:
        await message.answer("<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)

@router.callback_query(lambda x: x.data and x.data.startswith("users "))
async def each_opr(callback:CallbackQuery):
    check_creator=admin_functions.check_creator(user_id=callback.from_user.id)
    if check_creator==True:
        get_msg_id=admin_functions.get_msg_id(user_id=callback.from_user.id)
        get_operator=operator_functions.get_operator(user_id=callback.data.replace('users ',''))
        button=admin_kb.opr_btn(opr_id=callback.data.replace('users ',''))
        button2=admin_kb.opr_btn2(opr_id=callback.data.replace('users ',''))
        if get_operator.is_active==True:
            await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar</b>",chat_id=callback.from_user.id,message_id=get_msg_id,reply_markup=button,parse_mode=ParseMode.HTML) 
        else:
            await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar</b>",chat_id=callback.from_user.id,message_id=get_msg_id,reply_markup=button2,parse_mode=ParseMode.HTML)
    else:
        await bot.send_message(chat_id=callback.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
   


@router.callback_query(lambda x: x.data and x.data.startswith('del '))
async def remove_opr(callback:CallbackQuery):
    check_creator=admin_functions.check_creator(user_id=callback.from_user.id)
    if check_creator==True:
        get_msg_id=admin_functions.get_msg_id(user_id=callback.from_user.id)
        get_operator=operator_functions.get_operator(user_id=callback.data.replace('del ',''))
        await callback.answer(text=f"Operator\n{get_operator.user_name.capitalize()} o'chirildi",show_alert=True)
        operator_functions.remove_opr(user_id=get_operator.user_id)    
    
        time.sleep(1)          
        message_reply=admin_functions.message_reply()
        await bot.edit_message_text(chat_id=callback.from_user.id,text='<b>Operatorlar ro\'yhati</b>',reply_markup=message_reply,message_id=get_msg_id,parse_mode=ParseMode.HTML)
    else:
        await bot.send_message(chat_id=callback.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
   


@router.callback_query(lambda x: x.data and x.data.startswith('stat '))
async def statics(callback:CallbackQuery):
    check_creator=admin_functions.check_creator(user_id=callback.from_user.id)
    if check_creator==True:
        get_msg_id=admin_functions.get_msg_id(user_id=callback.from_user.id)
        get_operator=operator_functions.get_operator(user_id=callback.data.replace('stat ',''))
        await bot.edit_message_text(chat_id=callback.from_user.id,text=f"<b>Operator</b> - <i>{get_operator.user_name.capitalize()}</i>\n<b>Telefon raqami</b> - {get_operator.phone_number}\n<b>Shartnomalar soni</b> - <i>{get_operator.contracts_count}</i>",parse_mode=ParseMode.HTML,message_id=get_msg_id,reply_markup=admin_kb.back)
    else:
        await bot.send_message(chat_id=callback.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
   

@router.callback_query(lambda x: x.data and x.data.startswith('is_active '))
async def is_active_op(callback:CallbackQuery):
    check_creator=admin_functions.check_creator(user_id=callback.from_user.id)
    if check_creator==True:
        get_operator=operator_functions.get_operator(user_id=callback.data.replace('is_active ',''))
        admin_functions.op_is_active(opr_id=callback.data.replace('is_active ',''))
        new_info=operator_functions.get_operator(user_id=get_operator.user_id)
        button=admin_kb.opr_btn(opr_id=callback.data.replace('is_active ',''))
        button2=admin_kb.opr_btn2(opr_id=callback.data.replace('is_active ',''))
        get_msg_id=admin_functions.get_msg_id(user_id=callback.from_user.id)
        if get_operator.is_active==True:
            await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar</b>",chat_id=callback.from_user.id,message_id=get_msg_id,reply_markup=button2,parse_mode=ParseMode.HTML) 
        else:
            await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar</b>",chat_id=callback.from_user.id,message_id=get_msg_id,reply_markup=button,parse_mode=ParseMode.HTML)

        if new_info.is_active==True:
            await bot.send_message(chat_id=get_operator.user_id,text="<b>Siz botdan yana foydalana olasiz</b>",parse_mode=ParseMode.HTML)
        else:
            await bot.send_message(chat_id=get_operator.user_id ,text="<b>Siz bloklandiz</b>",parse_mode=ParseMode.HTML)
    else:
        await bot.send_message(chat_id=callback.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
   
@router.callback_query(lambda x:x.data and x.data.startswith('editName '))
async def Edit_Username_Operator(callback:CallbackQuery,state:FSMContext):
    check_creator=admin_functions.check_creator(user_id=callback.from_user.id)
    if check_creator==True:
        ms= await callback.message.answer(text="<b>Yangi ismni kiriting</b>",reply_markup=admin_kb.stop_Name,parse_mode=ParseMode.HTML)
        await state.set_state(Name.name)
        admin_functions.add_msg_id2(user_id=callback.from_user.id,msg_id=ms.message_id)
        admin_functions.last_opr_ID(user_id=callback.from_user.id,lastID=callback.data.replace('editName ',''))
        #get_oper=operator_functions.get_operator(user_id=callback.data.replace('editName ',''))
        #get_msg_id=admin_functions.get_msg_id(user_id=callback.from_user.id)
        #operator_functions.edit_name_operator(user_id=get_oper.user_id,new_name='dd')
        #get_operator=operator_functions.get_operator(user_id=callback.data.replace('editName ',''))
    
    else:
        await bot.send_message(chat_id=callback.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)

@router.message(Name.name)
async def state_edit_name_opr(message:Message,state:FSMContext):
    check_creator=admin_functions.check_creator(user_id=message.from_user.id)
    if check_creator==True:
        await state.update_data(name=message.text.upper())
        data=await state.get_data()
        get_creator=admin_functions.get_creator(user_id=message.from_user.id)
        operator_functions.edit_name_operator(user_id=get_creator.last_opr_id,new_name=data['name'])
        await state.clear()
        try:
            await bot.delete_messages(chat_id=message.from_user.id,message_ids=[get_creator.msg_id2,message.message_id])
        except:
            pass
        
        get_operator=operator_functions.get_operator(user_id=get_creator.last_opr_id)
        button=admin_kb.opr_btn(opr_id=get_operator.user_id)
        button2=admin_kb.opr_btn2(opr_id=get_operator.user_id)
        try:
            if get_operator.is_active==True:
                await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar ♻️</b>",chat_id=message.from_user.id,message_id=get_creator.msg_id,parse_mode=ParseMode.HTML,reply_markup=button) 
        
            else:
                await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar  ♻️</b>",chat_id=message.from_user.id,message_id=get_creator.msg_id,parse_mode=ParseMode.HTML,reply_markup=button2) 
        except:
            if get_operator.is_active==True:
                await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar  ♻️</b>",chat_id=message.from_user.id,message_id=get_creator.msg_id,parse_mode=ParseMode.HTML,reply_markup=button) 
        
            else:
                await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar ♻️</b>",chat_id=message.from_user.id,message_id=get_creator.msg_id,parse_mode=ParseMode.HTML,reply_markup=button2) 
    else:
        await bot.send_message(chat_id=message.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)


@router.callback_query(F.data=='sss')
async def ssss(callback:CallbackQuery,state:FSMContext):
    check_creator=admin_functions.check_creator(user_id=callback.from_user.id)
    if check_creator==True:
        get_creator=admin_functions.get_creator(user_id=callback.from_user.id)
        await callback.answer(text="Bekor qilindi",show_alert=True)
        current_state=await state.get_state()
        if current_state==None:
            return 
        await state.clear()
        try:
            await bot.delete_message(chat_id=callback.from_user.id,message_id=get_creator.msg_id2)
        except:
            pass
        get_operator=operator_functions.get_operator(user_id=get_creator.last_opr_id)
        button=admin_kb.opr_btn(opr_id=get_operator.user_id)
        button2=admin_kb.opr_btn2(opr_id=get_operator.user_id)
        try:
            if get_operator.is_active==True:
                await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar ♻️</b>",chat_id=callback.from_user.id,message_id=get_creator.msg_id,parse_mode=ParseMode.HTML,reply_markup=button) 
        
            else:
                await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar  ♻️</b>",chat_id=callback.from_user.id,message_id=get_creator.msg_id,parse_mode=ParseMode.HTML,reply_markup=button2) 
        except:
            if get_operator.is_active==True:
                await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar  ♻️</b>",chat_id=callback.from_user.id,message_id=get_creator.msg_id,parse_mode=ParseMode.HTML,reply_markup=button) 
        
            else:
                await bot.edit_message_text(text=f"<b>{get_operator.user_name} haqida ma'lumotlar ♻️</b>",chat_id=callback.from_user.id,message_id=get_creator.msg_id,parse_mode=ParseMode.HTML,reply_markup=button2) 
    else:
        await bot.send_message(chat_id=callback.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
   
@router.callback_query(F.data=='back')
async def back(callback:CallbackQuery):
    check_creator=admin_functions.check_creator(user_id=callback.from_user.id)
    if check_creator==True:
        get_msg_id=admin_functions.get_msg_id(user_id=callback.from_user.id)
        get_info_creator=admin_functions.get_info_creator(user_id=callback.from_user.id)
        message_reply=admin_functions.message_reply()
        if get_info_creator.last_button_text=='Foydalanuvchilar':
            await bot.edit_message_text(chat_id=callback.from_user.id,text='<b>Operatorlar ro\'yhati</b>',reply_markup=message_reply,message_id=get_msg_id,parse_mode=ParseMode.HTML)
    else:
        await bot.send_message(chat_id=callback.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
   
@router.message(F.text=='Referral')
async def deep_link(message:Message):
    check_creator=admin_functions.check_creator(user_id=message.from_user.id)
    if check_creator==True:
        unique_identifier=secrets.token_urlsafe(16)
        deep_link_url=f"{BOT_NICKNAME}?start={unique_identifier}"
        await bot.send_message(text=deep_link_url,chat_id=message.from_user.id)
    else:
        await bot.send_message(chat_id=message.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
      
@router.message(F.text=='Qidiruv')
async def find_customer(message:Message):
    check_creator=admin_functions.check_creator(user_id=message.from_user.id)
    if check_creator==True:
        get_all=customer_functions.get_customer_all()
        if len(get_all)!=None:
            msg_id=await bot.send_message(chat_id=message.from_user.id,text='<b>Mijozlar ro\'yhati</b>',reply_markup=admin_kb.inline_queyrbtn,parse_mode=ParseMode.HTML)       
            get_msg_id=admin_functions.get_msg_id(user_id=message.from_user.id)
            try:
                await bot.delete_message(chat_id=message.from_user.id,message_id=get_msg_id)
            except:
                pass
            admin_functions.add_msg(msg_id=msg_id.message_id,user_id=message.from_user.id)
        else:
            await bot.send_message(chat_id=message.from_user.id,text="<b>Xozircha ma'lumotlar yo'q</b>",parse_mode=ParseMode.HTML)
    else:
        await bot.send_message(chat_id=message.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
 



@router.message(F.text=='Statistika')
async  def statistika_all(message:Message):
    check_creator=admin_functions.check_creator(user_id=message.from_user.id)
    if check_creator==True:
        get_operator_al=operator_functions.get_operator_all()
        get_TRUE=operator_functions.operator_TRUE()
        get_CONT=customer_functions.get_customer_all()
        await message.answer(text=f"<b>SHartnomalar soni - {get_CONT.count()}\nOperatorlar soni - {get_TRUE.count()}\{get_operator_al.count()}</b>",parse_mode=ParseMode.HTML)
    
    else:
        await bot.send_message(chat_id=message.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
dp.include_router(inlines.router)


        