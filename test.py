import sqlite3


# conntect sqllite3
con = sqlite3.connect("data/users.db")
cursor = con.cursor()

# cursor.execute("""DELETE from users WHERE user_id = 5884447415""")
# print('delete succes')
cursor.execute("""CREATE TABLE IF NOT EXISTS users (user_id INT, referal_freinds_id TEXT, transfer_friends_id TEXT)""")
# cursor.execute(f"""INSERT INTO users VALUES (5752098078, '[]', '[]')""")

cursor.execute("""SELECT * FROM users""")
print(
    cursor.fetchall()
)

print(bool(1))
# con.commit()

# cursor.execute(f"""UPDATE users SET referal_freinds_id = 'salom'
#                 WHERE user_id = 5752098078
#     """)

# cursor.execute("""SELECT * FROM users WHERE user_id = 5752098078""")
# print(
#     cursor.fetchall()
# )














    # print(chek_member)

    # hoptimehomeshop
    
    # sql.execute(f"""SELECT * FROM users WHERE user_id = 9""")
    # user_auth_cheker = bool(sql.fetchall())
    # print(user_auth_cheker)

    

    # if not user_auth_cheker:
    #     sql.execute(f"""INSERT INTO users VALUES ({user_id})""")
    #     db.commit()
    
    # await message.answer(
    #     f"Assalomu alaykum, <a href='tg://user?id={user_id}'>{message.from_user.full_name}!</a>",
    #     reply_markup=ReplyKeyboardRemove()
    #     )
