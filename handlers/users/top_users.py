from aiogram import types
from loader import dp, bot
import sqlite3

db = sqlite3.connect('data/users.db')
sql = db.cursor()


@dp.callback_query_handler(text_contains="top_users")
async def callback_handler(query: types.CallbackQuery):

    user_id = query.message.from_user.id

    # user_id
    sql.execute(f"""SELECT rowid, * FROM users ORDER BY active_user_count DESC""")
    top_users = sql.fetchall()

    main_text = "❗️Top foydalanuvchilar\n\n"
    for i in top_users:
        res_user = await bot.get_chat(chat_id=i[1])
        main_text += f"""{i[0]}) <a href="tg://user?id={res_user.id}">{res_user.first_name}</a> active:{i[2]}, passive:{i[3]}\n"""

    await query.message.answer(text=main_text)