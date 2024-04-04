from aiogram.types import KeyboardButton,InlineKeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Bot.functions import operator_functions




admin_markup=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Foydalanuvchilar'),
            KeyboardButton(text='Qidiruv')
            
        ],
        [
            KeyboardButton(text='Referral'),
            KeyboardButton(text="Statistika")
           
        ]
    ],
    input_field_placeholder='Menu',
    resize_keyboard=True,
)


back=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='↩️',callback_data='back')]
    ]
)


def opr_btn(opr_id):
    btn=InlineKeyboardBuilder()
    btn.add(InlineKeyboardButton(text='Statistika',callback_data=f"stat {opr_id}")).add(InlineKeyboardButton(text="Bloklash ✅",callback_data=f"is_active {opr_id}")).row(InlineKeyboardButton(text="F.I.SH o'zgartirish ✏️",callback_data=f"editName {opr_id}")).row(InlineKeyboardButton(text="O'chirish ❌",callback_data=f"del {opr_id}")).row(InlineKeyboardButton(text='↩️',callback_data='back'))
    return btn.as_markup()

def opr_btn2(opr_id):
    btn=InlineKeyboardBuilder()
    btn.add(InlineKeyboardButton(text='Statistika',callback_data=f"stat {opr_id}")).add(InlineKeyboardButton(text="Blokdan chiqarish ⭕️",callback_data=f"is_active {opr_id}")).row(InlineKeyboardButton(text="F.I.SH o'zgartirish ✏️",callback_data=f"editName {opr_id}")).row(InlineKeyboardButton(text="O'chirish ❌",callback_data=f"del {opr_id}")).row(InlineKeyboardButton(text='↩️',callback_data='back'))
    return btn.as_markup()
inline_queyrbtn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Mizojlar haqida ma\'lumotlar',
            switch_inline_query_current_chat='customers')
            
        ]
    ]
)


def download_btn(cus_pk):
    download=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="PDF faylni yuklash 📥",callback_data=f'yuklash {cus_pk}')
            ]
        ]
    )
    return download

stop_Name=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bekor qilish",callback_data='sss')
        ]
    ]
)
