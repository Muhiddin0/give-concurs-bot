from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# obuna bo'lish va uni obuna bo'lganini tekshirish unchun btnlar
def subscribe_chanel_btn_fn(partnyor_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Hoptime Home shop', url="https://t.me/hoptimehomeshop"),
            ],
            [
                InlineKeyboardButton(text='✅ Tekshirish', callback_data=f"cheking_member:partnyorid_{str(partnyor_id)}")
            ]
        ]
    )


# asosiy settings btnlari
acc_setting_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Top 1 settings', callback_data=f"top_users_setting")
            ],
            [
                InlineKeyboardButton(text='✅ Tekshirish', callback_data=f"test")
            ]
        ]
    )


top1_usernameTrue = InlineKeyboardButton(text='✅ Foydalanuvchi nomingiz', callback_data=f"top_1_user_name")
top1_acc_linkTrue = InlineKeyboardButton(text='✅ Accountingiz ma\'nzili', callback_data=f"top_1_acc_link")

top1_usernameFalse = InlineKeyboardButton(text='❌ Foydalanuvchi nomingiz', callback_data=f"top_1_user_name")
top1_acc_linkFalse = InlineKeyboardButton(text='❌ Accountingiz ma\'nzili', callback_data=f"top_1_acc_link")




# menu btni
menu_btns = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='💸 Pul yechish', callback_data="pul_yechish"),
                InlineKeyboardButton(text='💰 Pul ishlash', callback_data="pul_ishlash"),
            ],
            [
                InlineKeyboardButton(text='🏆 Top foydalanuvchilar', callback_data="top_users"),
                InlineKeyboardButton(text='⚙️ Settings', callback_data="settings"),
            ]
        ]
    )
    

    