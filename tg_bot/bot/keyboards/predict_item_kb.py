from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

predict_item_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='🐕 Выбрать команду 🐈‍⬛'
        )
    ]
], resize_keyboard= True, one_time_keyboard= True, input_field_placeholder= 'Нажмите кнопоку ниже')
