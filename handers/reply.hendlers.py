from aiogram import types, Router

router = Router()

@router.message(lambda message: message.text == "Test")
async def test_handler(message: types.Message):
    await message.ANSSWER("""It's tet message!""")