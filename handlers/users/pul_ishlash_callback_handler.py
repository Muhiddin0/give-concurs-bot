from aiogram import types
from loader import dp


@dp.callback_query_handler(text_contains="pul_ishlash")
async def callback_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo=open("imgs/logo.jpg", "rb"),
        caption=f"""Salom men <a href='https://t.me/hoptimehomeshopbot?start={query['from']['id']}'>@hoptimehomeshopbot</a> man\nMeni sizga <a href='tg://user?id={query['from']['id']}'>{query['from']['first_name']}</a> Tafsiya qilmoqda \nSiz biz bilan pul ishlashingiz va servicesimizdan foydalanishingiz mumkin \n\nt.me/hoptimehomeshopbot?start={query['from']['id']}"""
    )

    # await query.message.answer(text=f"Sizning referalkangiz\n\nhttps://t.me/hoptimehomeshopbot?start={query['from']['id']}")
    await query.message.answer(text="Yuqoridagi postni do'stlaringizga ulashing va har bir kirgan odam uchun 1 ball oling")


