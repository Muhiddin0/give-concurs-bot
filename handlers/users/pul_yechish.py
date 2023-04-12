from aiogram import types
from loader import dp, bot
import sqlite3

db = sqlite3.connect('data/users.db')
sql = db.cursor()


@dp.callback_query_handler(text_contains="pul_yechish")
async def callback_handler(query: types.CallbackQuery):
    
    sql.execute(f"""SELECT * FROM users WHERE user_id = {query['from']['id']}""")
    user_data = sql.fetchall()[0]

    await query.message.answer(text=f"Sizning hissobingizda {user_data[1]} ball bor")
    
