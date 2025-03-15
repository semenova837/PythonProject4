from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
def get_main_keyboard()-> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMurkup(
        keyboard = [
            [KeyboardButton(text="Test")]
        ],
        resize_keyboard=True
    )
    return keyboard