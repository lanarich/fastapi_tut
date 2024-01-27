from aiogram.utils.keyboard import InlineKeyboardBuilder


def place_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text=f"👋 Приветствие 👋", callback_data=f"set:1")
    kb.button(text=f"📊 База данных собак 📊", callback_data=f"set:2")
    kb.button(text=f"🐶 Собаки определенной породы 🐶", callback_data=f"set:3")
    kb.button(text=f"✏️ Добавить собаку ✏️", callback_data=f"set:4")
    kb.button(text=f"🔢 Вывести собаку с определенным id 🔢", callback_data=f"set:5")
    kb.button(text=f"🛠️ Изменить данные собаки 🛠️", callback_data=f"set:6")
    kb.adjust(1)
    return kb.as_markup()


