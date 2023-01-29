from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_keyboard = InlineKeyboardMarkup()

sub_admin_keyboard = InlineKeyboardMarkup()

statistics_button = InlineKeyboardButton(text="Статистика", callback_data="statistics")
all_time_button = InlineKeyboardButton(text="За все время", callback_data="all_time")
last_7_days_button = InlineKeyboardButton(text="Последние 7 дней", callback_data="last_7_days")

admin_keyboard.add(statistics_button)
sub_admin_keyboard.add(all_time_button)
sub_admin_keyboard.add(last_7_days_button)


