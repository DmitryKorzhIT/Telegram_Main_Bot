from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hcode
from aiogram.dispatcher.filters import Text
import pandas as pd
import numpy as np

from code.config import telegram_token


bot = Bot(token=telegram_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# Get a message with a random movie.
def random_movie_value():

    # Read a csv file and create a random number.
    file = pd.read_csv('.data/kinopoisk_movies.csv')
    file_len = file[file.columns[0]].count() - 1
    random_value = np.random.randint(0, file_len)

    # Get link on a poster.
    image_link = file['posterUrl'][random_value]

    # Test description.
    test_description = 'Фантастический эпос про задыхающуюся Землю, космические ' \
                       'полеты и парадоксы времени. «Оскар» за спецэффекты'

    # Message view using aiogram markdown.
    text_value = f"{hbold(file['nameRu'][random_value])} " \
                 f"{hbold('(')}{hbold(file['year'][random_value])}{hbold(')')}\n\n" \
                 f"\U0001F31F{hcode(' Рейтинг:')}   {hbold(file['ratingKinopoisk'][random_value])}\n" \
                 f"\U0001F440{hcode(' Оценки:')}     {hbold('523K')}\n" \
                 f"\U0000231B{hcode(' Время:')}       {hbold('169 мин.')}\n\n" \
                 f"\U0001F4D6{hcode(' Описание:')} {test_description}"

    message_list = [image_link, text_value]

    return message_list



# Inline buttons for a message with a random movie.
def random_movie_buttons():

    # Message inline buttons.
    buttons = [types.InlineKeyboardButton(text="<", callback_data="previous_movie"),
               types.InlineKeyboardButton(text=">", callback_data="next_movie")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard












