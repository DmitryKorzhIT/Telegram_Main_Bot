from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink, hspoiler
from config import telegram_token
from aiogram.dispatcher.filters import Text
import pandas as pd
import numpy as np


bot = Bot(token=telegram_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# Handler for pressing a "type of movies" button.
@dp.message_handler(commands='start')
async def type_of_movies_button(message: types.Message):
    buttons = ['Фильмы / Сериалы', 'Пропустить Ф/С']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    type_of_movies_value = ('Пожалуйста, выберите из списка ниже' + u'\U0001F447')
    await message.answer(type_of_movies_value, reply_markup=keyboard)


# Handler for type of movies.
@dp.message_handler(Text(equals="Фильмы / Сериалы"))
async def type_of_movies(message: types.Message):
    type_of_movies_value = ("Фильмы (/4j51b)\n"
                            "Мультфильмы (/8ba8o)\n"
                            "Сериалы (/3l51v)\n"
                            "Аниме (/jas82)\n")
    await message.answer(type_of_movies_value)


# Handler for pressing a "genre" button.
@dp.message_handler(Text(equals="Пропустить Ф/С"))
@dp.message_handler(commands='4j51b')
@dp.message_handler(commands='8ba8o')
@dp.message_handler(commands='3l51v')
@dp.message_handler(commands='jas82')
async def genre_button(message: types.Message):
    buttons = ['Жанры', 'Пропустить жанры']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    genre_value = ('Выберите жанры' + u'\U0001F447')
    await message.answer(genre_value, reply_markup=keyboard)


# Handler for choosing a genre.
@dp.message_handler(Text(equals="Жанры"))
async def genre(message: types.Message):
    genre_value = ("Фантастика (/4j851b)\n"
                   "Мюзикл (/3l851v)\n")
    await message.answer(genre_value)


# Handler for pressing a "year" button.
@dp.message_handler(Text(equals="Пропустить жанры"))
@dp.message_handler(commands='4j851b')
@dp.message_handler(commands='3l851v')
async def year_button(message: types.Message):
    buttons = ['Года', 'Пропустить года']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    year_value = ('Выберите года:' + u'\U0001F447')
    await message.answer(year_value, reply_markup=keyboard)


# Handler for choosing a year.
@dp.message_handler(Text(equals="Года"))
async def year(message: types.Message):
    year_value = ("До 2000 (/XCNpkmy5)\n"
                  "2000 - 2010 (/HFUyun2u)\n"
                  "2011 - 2020 (/vCJ0Dn9z)\n"
                  "2021 - 2022 (/tkpn4YUf)\n")
    await message.answer(year_value)


# Handler for pressing a "kinopoisks raiting" button.
@dp.message_handler(Text(equals="Пропустить года"))
@dp.message_handler(commands='XCNpkmy5')
@dp.message_handler(commands='HFUyun2u')
@dp.message_handler(commands='vCJ0Dn9z')
@dp.message_handler(commands='tkpn4YUf')
async def kinopoisk_raiting_button(message: types.Message):
    buttons = ['Рейтинг Кинопоиска', 'Пропустить рейтинг']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    kinopoisk_raiting = ('Выберите рейтинг кинопоиска:' + u'\U0001F447')
    await message.answer(kinopoisk_raiting, reply_markup=keyboard)


# Handler for choosing a kinopoisk raiting.
@dp.message_handler(Text(equals="Рейтинг Кинопоиска"))
async def kinopoisk_raiting(message: types.Message):
    raiting_value = ("До 6.0 (/Fi3ocz8K)\n"
                    "6.0 - 6.9 (/X2sqFxj9)\n"
                    "7.0 - 7.5 (/AhdFB2e4)\n"
                    "7.6 - 7.9 (/Fi5az1kq)\n"
                    "8.0 и более (/C31BjQyY)")
    await message.answer(raiting_value)


# Handler for pressing a "showing results" button.
@dp.message_handler(Text(equals="Пропустить рейтинг"))
@dp.message_handler(commands='Fi3ocz8K')
@dp.message_handler(commands='X2sqFxj9')
@dp.message_handler(commands='AhdFB2e4')
@dp.message_handler(commands='Fi5az1kq')
@dp.message_handler(commands='C31BjQyY')
async def random_movie(message: types.Message):

    # Read a csv file and create a random number.
    file = pd.read_csv('./.data/netflix_titles.csv')
    file_len = file[file.columns[0]].count() - 1
    random_value = np.random.randint(0, file_len)

    # Message view using aiogram markdown.
    random_movie_value = f"{hbold(file['title'][random_value])} " \
                         f"({file['release_year'][random_value]})\n" \
                         f"{file['description'][random_value]}"

    await message.answer(random_movie_value, reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    print('It is working!')
    executor.start_polling(dp, skip_updates=True)
