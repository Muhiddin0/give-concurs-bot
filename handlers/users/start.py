

# bot
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import bot
from aiogram.types import chat_member


# inline markups
from keyboards.inline.inline_btns import subscribe_chanel_btn_fn, menu_btns

# local bor
from loader import dp

from .user_add_counter import counter_user




# shartlar
# grupda va kanalga obuna bo'lgan bo'lishi kerak
# eski yoki yangi foydalanuvchiligini tekshirish kerak
# kim tomonidan taklif qilinganini bilish kerak
# 


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    user_id = message.from_user.id
    partnyor_id = message.get_args() if message.get_args() != "" else 404


    member_chek_status = await bot.get_chat_member(chat_id="@hoptimehomeshop", user_id=user_id)
    if member_chek_status['status'] == "left":
        await message.answer_photo(
                photo=open("imgs/logo.jpg", "rb")  ,
                caption=f"<b>👋 Salom </b><a href='tg://user?id={user_id}'>{message.from_user.first_name}</a><b> !\n\nBotdan to'liq foydalanish uchun \nkanalimizga obuna bo'lishingiz za'rur</b>",
                reply_markup=subscribe_chanel_btn_fn(partnyor_id),
            )
        return
    
    await counter_user(message, user_id, partnyor_id)