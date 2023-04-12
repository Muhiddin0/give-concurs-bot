
# bot
from loader import bot


# inlin markups
from keyboards.inline.inline_btns import menu_btns

# sqlite3 
import sqlite3

db = sqlite3.connect('data/users.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (user_id INT, active_user_count INT, passive_user_count INT, top_show_title INT, top_show_link INT)""")
db.commit()




async def counter_user(message, user_id, partnyor_id):

    # foydalanuvchini bazadan qidirish 
    sql.execute(f"""SELECT rowid, * FROM users WHERE user_id = {user_id}""")
    user_data = sql.fetchall()
    

    # foydalanuvchi bazada bor yo'qligini tekshirish
    if bool(user_data):
        await message.answer("Siz konkursizmizda qatnashmoqdasiz")        
        await message.answer(text=f"""🟢 Asosiy Menu""", reply_markup=menu_btns)
        return


    # foydalanuvchi bazada yo'q bo'lsa uni bazaga kiritish
    sql.execute(f"""INSERT INTO users VALUES ({user_id}, 0, 0, 1, 1)""")
    db.commit()
    
    
    # taklif qilingan foydalnuvchini referal do'stiga ball berish
    sql.execute(f"""SELECT * FROM users WHERE user_id = {partnyor_id}""")
    add_ball_user = sql.fetchall()


    # bazada taklif qiluvchi topilmasa apiratsiani tugatish
    if not bool(add_ball_user):
        await message.answer(text=f"""🟢 Asosiy Menu""", reply_markup=menu_btns)    
        return

    await bot.send_message(chat_id=partnyor_id, text=f'''Tabriklayman do'tingiz <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>\nShartlarni bajarib sizga ➕1️⃣ ball olib keldi''')


    user_ball = add_ball_user[0][1] +1
    
    sql.execute(f"""UPDATE users SET active_user_count = {user_ball}
                    WHERE user_id = {partnyor_id}
        """)
    db.commit()

    # asosiy menuni chiqarish
    await message.answer(
        text=f"""🟢 Asosiy Menu""",
        reply_markup=menu_btns
        )    
