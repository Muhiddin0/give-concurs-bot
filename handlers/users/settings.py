from aiogram import types
from loader import dp, bot

# btns
from keyboards.inline.inline_btns import(
    acc_setting_btn,

    top1_usernameTrue,
    top1_usernameFalse,


    top1_acc_linkTrue,
    top1_acc_linkFalse,
    )
from aiogram.types import InlineKeyboardMarkup

# baza
import sqlite3
db = sqlite3.connect('data/users.db')
sql = db.cursor()


@dp.callback_query_handler(text_contains="settings")
async def callback_handler(query: types.CallbackQuery):

    await query.message.answer(text="setting bo'limi yaqin kunlarda ishga tushadi")
    return

    
    sql.execute(f"""SELECT * FROM users WHERE user_id = {query['from']['id']}""")
    user_data = sql.fetchall()[0]
    
    acc_name_status = {"btn":top1_usernameTrue, "text":"✅ Foydalanuvchi nomingiz"} if user_data[3] else {"btn":top1_usernameFalse, "text":"❌ Foydalanuvchi nomingiz"}
    acc_link_status = {"btn":top1_acc_linkTrue, "text":"✅ Foydalanuvchi nomingiz"} if user_data[4] else {"btn":top1_acc_linkFalse, "text":"❌ ✅ Accountingiz ma'nzili"}

    await query.message.edit_text(
        text=f"⚙️ Settings\n\nTop foydalanuvchilar\n{acc_name_status['text']}\n{acc_link_status['text']}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                acc_link_status['btn'],
                acc_link_status['btn']
            ])
        )
    

@dp.callback_query_handler(text_contains="top_users_setting")
async def callback_handler(query: types.CallbackQuery):

    sql.execute(f"""SELECT * from users WHERE user_id = {query.message.from_user.id}""")
    user_data = sql.fetchall()[0]

    await query.message.edit_text(
        text=f"""settings \n\n{"✅ Foydalanuvchi nomingiz" if user_data[3] else "❌ Foydalanuvchi nomingiz"}\n{"✅ Accountingiz ma'nzili" if user_data[3] else "❌ ✅ Accountingiz ma'nzili"}""",
        reply_markup=top_1_btn
        )
    
    