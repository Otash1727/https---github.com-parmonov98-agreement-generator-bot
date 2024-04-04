from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove
from shop.models import Customer

contact_markup=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Share contact',request_contact=True)]
    ],
    resize_keyboard=True,
    input_field_placeholder='Siz bilan bog\'lana oladigan nomerni  yuboring ',
   
)

operator_markup=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yangi shartnoma yaratish"),
            KeyboardButton(text="Qidiruv (shartnomalar)")
        ],
    ],
    input_field_placeholder="Buyruqlarni tanlang",
    resize_keyboard=True,
    
)


contract_markup=InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='Boshlash',callback_data='begin')
        ]
    ]  
)

def customer_info_edit(cont_id):
    get_id=Customer.objects.get(contract_number=cont_id)
    new_contract=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='F.I.SH',callback_data=f'full_name {get_id.contract_number}'),
                InlineKeyboardButton(text='Yashash joyi',callback_data=f'place_of {get_id.contract_number}')
            ],
            [
                InlineKeyboardButton(text='Telefon raqami',callback_data=f"phone_number {get_id.contract_number}"),
                InlineKeyboardButton(text="Pasport ma'lumotlari (Seriyasi)",callback_data=f"pass_info {get_id.contract_number}"),
            ],
            [    
                InlineKeyboardButton(text='Password berilgan vaqt',callback_data=f"pass_date {get_id.contract_number}"),
            ],
            [
                InlineKeyboardButton(text="Mahsulot nomi",callback_data=f"items {get_id.contract_number}"),
                InlineKeyboardButton(text="Umumiy narx",callback_data=f"total_p {get_id.contract_number}")
            ],
            [
                InlineKeyboardButton(text='Oldindan to\'lov',callback_data=f"advanced_pay {get_id.contract_number}"),
                InlineKeyboardButton(text="Umumiy qarzdorlik",callback_data=f"total_d {get_id.contract_number}")
            ],
            [
                InlineKeyboardButton(text="Oylik to'lov",callback_data=f"monthly_p {get_id.contract_number}"),    
                InlineKeyboardButton(text="Oylar Soni",callback_data=f'month {get_id.contract_number}')
            ],
            [
                InlineKeyboardButton(text="↩️",callback_data=f'back_pdf {get_id.contract_number}')
            ]
        ]
    )
    return new_contract


remove=ReplyKeyboardRemove(remove_keyboard=True,selective=True)


admin_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Admin bilan bog'lanish",switch_inline_query_current_chat='connect')]
    ]
)

remove_state=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Bekor qilish',callback_data='cancel')]
    ]
)


def stop_state(cont_id):
    get_id=Customer.objects.get(contract_number=cont_id)
    mark_up=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Bekor qilish',callback_data=f'stop {get_id.contract_number}')
            ]
        ]
    )
    return mark_up

search_operator=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Shartnomalarni qidirish",switch_inline_query_current_chat="search#")]
    ]
)