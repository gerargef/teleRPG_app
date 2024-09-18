import sqlite3
import logging

import config
from config import *
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, MessageHandler, filters

# Включаем логирование для отладки
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = config.TOKEN


# Функция, которая выполняет логику при нажатии кнопки "Старт"
async def start(update: Update, context) -> None:
    # Создаем кастомную клавиатуру с другими кнопками
    keyboard_1 = [
        [KeyboardButton("Действие 1"), KeyboardButton("Действие 2")],
        [KeyboardButton("Перейти к другой клавиатуре")]
    ]

    # Создаем разметку клавиатуры
    reply_markup = ReplyKeyboardMarkup(keyboard_1, resize_keyboard=True, one_time_keyboard=False)

    # Отправляем сообщение с новыми кнопками
    await update.message.reply_text('Выберите действие:', reply_markup=reply_markup)


# Функция для второй клавиатуры
async def second_keyboard(update: Update, context) -> None:
    # Вторая кастомная клавиатура
    keyboard_2 = [
        [KeyboardButton("Действие 3"), KeyboardButton("Действие 4")],
        [KeyboardButton("Назад к первой клавиатуре")]
    ]

    # Создаем разметку второй клавиатуры
    reply_markup = ReplyKeyboardMarkup(keyboard_2, resize_keyboard=True, one_time_keyboard=False)

    # Отправляем сообщение с второй клавиатурой
    await update.message.reply_text('Вы перешли к другой клавиатуре. Выберите действие или вернитесь назад:', reply_markup=reply_markup)


# Обработка действия 1
async def action_one(update: Update, context) -> None:
    await update.message.reply_text('Вы выбрали Действие 1!')


# Обработка действия 2
async def action_two(update: Update, context) -> None:
    await update.message.reply_text('Вы выбрали Действие 2!')


# Обработка действия 3
async def action_three(update: Update, context) -> None:
    await update.message.reply_text('Вы выбрали Действие 3!')


async def action_four(update: Update, context) -> None:
    await update.message.reply_text('Вы выбрали Действие 4!')




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

    # Обработчик для перехода на вторую клавиатуру
    application.add_handler(MessageHandler(filters.Text("Перейти к другой клавиатуре"), second_keyboard))


    application.add_handler(MessageHandler(filters.Text("Действие 3"), action_three))
    application.add_handler(MessageHandler(filters.Text("Действие 4"), action_four))

    # Обработчик для возврата к первой клавиатуре
    application.add_handler(MessageHandler(filters.Text("Назад к первой клавиатуре"), start))

    # Запускаем бота в режиме polling
    application.run_polling()


if __name__ == '__main__':
    main()
