import sqlite3
import logging

import config
from config import *
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, MessageHandler, filters

# Включаем логирование для отладки
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# with sqlite3.connect("test_db.sqlite") as connection:
#     cursor = connection.cursor()
#
#     query = """
#     DROP TABLE test
#     """
#
#     cursor.execute(query)

TOKEN = config.TOKEN


# Функция, которая выполняет логику при нажатии кнопки "Старт"
async def start(update: Update, context) -> None:
    # Создаем кастомную клавиатуру с другими кнопками
    custom_keyboard = [
        [KeyboardButton("Действие 1"), KeyboardButton("Действие 2")],
        [KeyboardButton("Действие 3")]
    ]

    # Создаем разметку клавиатуры
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True, one_time_keyboard=False)

    # Отправляем сообщение с новыми кнопками
    await update.message.reply_text('Выберите действие:', reply_markup=reply_markup)


# Обработка действия 1
async def action_one(update: Update, context) -> None:
    await update.message.reply_text('Вы выбрали Действие 1!')


# Обработка действия 2
async def action_two(update: Update, context) -> None:
    await update.message.reply_text('Вы выбрали Действие 2!')


# Обработка действия 3
async def action_three(update: Update, context) -> None:
    await update.message.reply_text('Вы выбрали Действие 3!')


# Основная функция для запуска бота
def main():
    # Создаем приложение для работы с ботом
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик для старта (автоматически показывает кнопку "Старт" при первом взаимодействии)

    # Обрабатываем нажатие на кнопку "Старт"
    application.add_handler(MessageHandler(filters.Text("/start"), start))  # Выполняем логику кнопки "Старт"

    # Обрабатываем действия
    application.add_handler(MessageHandler(filters.Text("Действие 1"), action_one))
    application.add_handler(MessageHandler(filters.Text("Действие 2"), action_two))
    application.add_handler(MessageHandler(filters.Text("Действие 3"), action_three))

    # Запускаем бота в режиме polling
    application.run_polling()


if __name__ == '__main__':
    main()
