from Bot.create_bot import dp,bot
from aiogram import Router,F
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,InlineKeyboardButton,ChatMemberUpdated
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.enums import ParseMode 
from Bot.functions import admin_functions,operator_functions
from Bot.handlers.admin import admin_scripts
from Bot.handlers.operator import operator_scripts
from Bot.keyboards import admin_kb,operator_kb 
from Bot.handlers.set_commands import set_commands
import time



import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

class Form(StatesGroup):
    phone=State()


router=Router()




@router.message(Command('start'))
async def run_bot(message:Message,state:FSMContext):
    check_creator=admin_functions.check_creator(user_id=message.from_user.id)
    check_operator=operator_functions.check_operator(user_id=message.from_user.id)
    if check_creator==True:
        await bot.send_message(chat_id=message.from_user.id,text="<b>Admin Paneliga xush kelibsiz</b>",reply_markup=admin_kb.admin_markup,parse_mode=ParseMode.HTML)
        await set_commands.set_commands(message=message.from_user.id)
        user=await bot.get_chat(chat_id=message.from_user.id)
        if user.username:
            admin_functions.add_username_admin(Username=user.username,user_id=message.from_user.id)
        else:
            pass
       
    elif check_operator==True:
        get_operator=operator_functions.get_operator(user_id=message.from_user.id)
        if get_operator.is_active==True:  
            await bot.send_message(text=f"<b>{get_operator.user_name.capitalize()} siz operator panelidasiz</b>",reply_markup=operator_kb.operator_markup,parse_mode=ParseMode.HTML,chat_id=message.from_user.id)
        else:
            await bot.send_message(chat_id=message.from_user.id,text=f'<b>{get_operator.user_name} sizda cheklovlar bor\nAdmin bilan bo\'g\'laning</b>',reply_markup=operator_kb.admin_inlin,parse_mode=ParseMode.HTML)

    elif len(message.text)>6:
        ref_link=message.text[6:]
        check_ref_link=operator_functions.check_ref_link(ref_link=ref_link)
        if check_ref_link==True:
            await bot.send_message(chat_id=message.from_user.id,text='Bu linkdan oldin foydalanilgan')
            await set_commands.set_commands(message=message.from_user.id)
            
        else:
            await bot.send_message(chat_id=message.from_user.id,text="<b>Operator paneliga xush kelibsiz</b>\n<b>Botdan foydalanish uchun telefon raqamizni yuboring</b>\n<i>Xohlang yozib yuboring xohlang tugmacha orqali</i>",reply_markup=operator_kb.contact_markup,parse_mode=ParseMode.HTML)
            operator_functions.add_reff_link(ref_link=ref_link)
            operator_functions.add_operator(user_id=message.from_user.id,user_name=message.from_user.full_name)
            await state.set_state(Form.phone)

    else:
        await bot.send_message(chat_id=message.from_user.id,text=f"<b>{message.from_user.full_name}</b>",reply_markup=operator_kb.remove,parse_mode=ParseMode.HTML)   


@router.message(Command('menu'))
async def command_menu(message:Message):
    check_operator=operator_functions.check_operator(user_id=message.from_user.id)
    check_creator=admin_functions.check_creator(user_id=message.from_user.id)
    if check_creator==True:
            await message.answer("<b>Buyruqlarni tanlang</b>",reply_markup=admin_kb.admin_markup,parse_mode=ParseMode.HTML)
    elif check_operator ==True:
            await  message.answer("<b>Buyruqlarni tanlang</b>",reply_markup=operator_kb.operator_markup,parse_mode=ParseMode.HTML)
    else:
        pass

def textToPhoneValidate(message: Message):
    return message.contact is not None or (message.text.startswith('+') and len(message.text) ==13)

@router.message(Form.phone)
async def input_phone(message:Message,state:FSMContext):
    if not textToPhoneValidate(message):
        return await message.answer('<b>Siz xato nomer kiritayapsiz \n For example: +998.........</b>   ',reply_markup=operator_kb.contact_markup,parse_mode=ParseMode.HTML)
    phoneNumber = message.contact.phone_number if message.contact is not None else message.text
    await state.update_data(phone=phoneNumber)
    data= await state.get_data()
    
    operator_functions.add_phone(user_id=message.from_user.id,phone=data['phone'])
    await state.clear()
    await bot.send_message(chat_id=message.from_user.id,text=f"<b>Siz ro'yhatdan o'tdingiz</b>",parse_mode=ParseMode.HTML,reply_markup=operator_kb.operator_markup)

dp.include_router(admin_scripts.router)
dp.include_router(operator_scripts.router)



