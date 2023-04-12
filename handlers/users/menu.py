

# bot
from aiogram import types
from loader import bot, dp


# inline markups
from keyboards.inline.inline_btns import menu_btns


# connect data base
import sqlite3
db = sqlite3.connect("data/users.db")
sql = db.cursor()


@dp.message_handler(commands=['menu'])
async def bot_start(message: types.Message):

    sql.execute(f"""SELECT * FROM users WHERE user_id = {message.from_user.id} """)    
    user_data = sql.fetchall()
    print(user_data)
    print(user_data[0][1])

    await message.answer(
        text=f"""🟢 Asosiy Menu\n\nBallaringiz: <b>{user_data[0][1]}</b>\nballaringiz: {user_data[0][1] * 1000} O'zbek so'm bo'ladi\nChiqarib oldingiz {user_data[0][2] * 1000} so'm""",
        reply_markup=menu_btns
        )