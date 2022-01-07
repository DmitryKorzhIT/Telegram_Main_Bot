from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import hbold
import pandas as pd
import numpy as np

from code.config import telegram_token


bot = Bot(token=telegram_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


def random_movie_value():

    # Read a csv file and create a random number.
    file = pd.read_csv('./.data/netflix_titles.csv')
    file_len = file[file.columns[0]].count() - 1
    random_value = np.random.randint(0, file_len)

    # Message view using aiogram markdown.
    random_movie_value = f"{hbold(file['title'][random_value])} " \
                         f"({file['release_year'][random_value]})\n" \
                         f"{file['description'][random_value]}"
    return random_movie_value


def random_movie_buttons():

    # Message inline buttons.
    buttons = [types.InlineKeyboardButton(text="<", callback_data="previous_movie"),
               types.InlineKeyboardButton(text=">", callback_data="next_movie")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard