

# bot
from aiogram import types
from loader import dp


# inline markups
from keyboards.inline.inline_btns import menu_btns


# import sql data/base
import sqlite3

# add user counter functi
from .user_add_counter import counter_user



# conntect sqllite3
# db = sqlite3.connect("data/users.db")
# sql = db.cursor()
# sql.execute("""CREATE TABLE IF NOT EXISTS users (user_id INT, referal_freinds_id TEXT, transfer_friends_id TEXT)""")

@dp.callback_query_handler(text_contains="cheking_member")
async def callback_handler(query: types.CallbackQuery):


    # callback datalar
    user_id = query.from_user.id
    callback_data_split = (query.data).split(':')
    partnyor_id = callback_data_split[1].split('_')[1]

    await counter_user(query.message, user_id, partnyor_id)

    