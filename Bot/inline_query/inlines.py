from Bot.create_bot import bot
from aiogram.types import InlineQuery,InlineQueryResultArticle,InputTextMessageContent,CallbackQuery,FSInputFile,Message,User
from aiogram.enums import ParseMode
from aiogram import Router,F
from Bot.functions import customer_functions,admin_functions,operator_functions
from Bot.keyboards import admin_kb,operator_kb


router=Router()


@router.inline_query(F.query.startswith('customers') or F.query.startswith('customers ') or F.query.startswith('customers  ') or F.query.startswith('customers   '))
async def search_admin(query:InlineQuery):
    check_creator=admin_functions.check_creator(user_id=query.from_user.id)
    if check_creator==True:
        split=query.query.split('customers')
        if split[1] is not None:
            get_customers=customer_functions.search_customer_byAdmin(query=query)
            results=[InlineQueryResultArticle(id=str(i.pk),title=f"Shartnoma raqami - {i.contract_number}",description=f"F.I.SH - {i.full_name}\nTelefon raqam - {i.phone_number}\n{i.which_operator} tomonidan",input_message_content=InputTextMessageContent(message_text=f"<b>F.I.SH - {i.full_name}\nYashash manzili - {i.place_of_residence}\nTelefon raqami - {i.phone_number}\nPasport(Seriyasi) - {i.passport_infos}\nPasport berilgan vaqti - {i.date_of_issue}\nMahsulot nomi - {i.item_name}\nOldindan to'lov - {i.advance_payment}\nUmumiy qarz - {i.total_debt}\nMahsulotni umumiy narxi - {i.total_price}\nOylik to'lov - {i.montly_payment}\nOylar soni - {i.months} </b>",parse_mode=ParseMode.HTML),reply_markup=admin_kb.download_btn(cus_pk=i.pk))for i in get_customers]
            await query.answer(results=results,is_personal=True)
           

        else:    
            get_customers=customer_functions.get_customer_all()
            results=[InlineQueryResultArticle(id=str(i.pk),title=f"Shartnoma raqami - {i.contract_number}",description=f"F.I.SH - {i.full_name}\nTelefon raqam - {i.phone_number}\n{i.which_operator} tomonidan",input_message_content=InputTextMessageContent(message_text=f"<b>F.I.SH - {i.full_name}\nYashash manzili - {i.place_of_residence}\nTelefon raqami - {i.phone_number}\nPasport(Seriyasi) - {i.passport_infos}\nPasport berilgan vaqti - {i.date_of_issue}\nMahsulot nomi - {i.item_name}\nOldindan to'lov - {i.advance_payment}\nUmumiy qarz - {i.total_debt}\nMahsulotni umumiy narxi - {i.total_price}\nOylik to'lov - {i.montly_payment}\nOylar soni - {i.months} </b>",parse_mode=ParseMode.HTML),reply_markup=admin_kb.download_btn(cus_pk=i.pk))for i in get_customers]
            await query.answer(results=results,is_personal=True)
    else:
        pass



@router.callback_query(lambda x: x.data and x.data.startswith('yuklash '))
async def download_customer_info(callback:CallbackQuery):
    check_creator=admin_functions.check_creator(user_id=callback.from_user.id)
    if check_creator==True: 
        cont_id=callback.data.replace('yuklash ','')
        get_costumer=customer_functions.get_customer(cont_id=cont_id)
        if get_costumer.File_ID is not None:
            await bot.send_document(chat_id=callback.from_user.id,document=f"{get_costumer.File_ID}",caption="Muvafaqiyatli ✅")
        else:
            await bot.send_message(chat_id=callback.from_user.id,text="<b>Ma'lumot topilmadi</b>",parse_mode=ParseMode.HTML)
    else:
        await bot.send_message(chat_id=callback.from_user.id,text="<b>Siz admin emassiz\nSog' bo'ling</b>",parse_mode=ParseMode.HTML)
 
@router.inline_query(F.query=='connect')
async def deep_link_admin(query:InlineQuery):
    check_operator=operator_functions.check_operator(user_id=query.from_user.id)
    
    if check_operator==True:
        get_admin=admin_functions.get_creator_all()
        results=[InlineQueryResultArticle(id=str(i.user_id),title=f"Admin - {i.user_name}",description="Bo'glanish uchun",input_message_content=InputTextMessageContent(message_text=f"Admin - {i.user_name}\nBog'lanish - https://t.me/{i.username}",parse_mode=ParseMode.HTML))for i in get_admin]
        await query.answer(results=results,is_personal=True)
    else:
        await operator_functions.fake_operator(chat_id=query.from_user.id)

@router.inline_query(F.query.startswith('search#'))
async def search_operator(query:InlineQuery):
    check_oper=operator_functions.check_operator(user_id=query.from_user.id)
    if check_oper==True:
        get_opr=operator_functions.get_operator(user_id=query.from_user.id)
        if get_opr.is_active==True:
            split_query=query.query.split('search#')
            if split_query[1] is not None:
                get_sdd=customer_functions.search_customer(query=query,oper_id=get_opr.user_id)
                result=[InlineQueryResultArticle(id=str(i.pk),title=f"Shartnoma raqami - {i.contract_number}",description=f"F.I.SH - {i.full_name}\nTelefon raqam - {i.phone_number}",input_message_content=InputTextMessageContent(message_text=f"<b>F.I.SH - {i.full_name}\nYashash manzili - {i.place_of_residence}\nTelefon raqami - {i.phone_number}\nPasport(Seriyasi) - {i.passport_infos}\nPasport berilgan vaqti - {i.date_of_issue}\nMahsulot nomi - {i.item_name}\nOldindan to'lov - {i.advance_payment}\nUmumiy qarz - {i.total_debt}\nMahsulotni umumiy narxi - {i.total_price}\nOylik to'lov - {i.montly_payment}\nOylar soni - {i.months} </b>",parse_mode=ParseMode.HTML),reply_markup=customer_functions.customer_message_reply2(cont_id=i.contract_number))for i in get_sdd]
                await query.answer(results=result,is_personal=True)
            
            else:
                get_customers=customer_functions.get_customer_WhichOpr(opr_id=query.from_user.id)
                result=[InlineQueryResultArticle(id=str(i.pk),title=f"Shartnoma raqami - {i.contract_number}",description=f"F.I.SH - {i.full_name}\nTelefon raqam - {i.phone_number}",input_message_content=InputTextMessageContent(message_text=f"<b>F.I.SH - {i.full_name}\nYashash manzili - {i.place_of_residence}\nTelefon raqami - {i.phone_number}\nPasport(Seriyasi) - {i.passport_infos}\nPasport berilgan vaqti - {i.date_of_issue}\nMahsulot nomi - {i.item_name}\nOldindan to'lov - {i.advance_payment}\nUmumiy qarz - {i.total_debt}\nMahsulotni umumiy narxi - {i.total_price}\nOylik to'lov - {i.montly_payment}\nOylar soni - {i.months} </b>",parse_mode=ParseMode.HTML),reply_markup=customer_functions.customer_message_reply2(cont_id=i.contract_number))for i in get_customers]
                await query.answer(results=result,is_personal=True)
            
        else:
            await operator_functions.is_active_message(user_id=query.from_user.id,chat_id=query.from_user.id)
    else:
        await operator_functions.fake_operator(chat_id=query.from_user.id,text=query.from_user.full_name)

