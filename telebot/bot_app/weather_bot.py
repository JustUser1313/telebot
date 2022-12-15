from django.core.management.base import BaseCommand
from django.conf import settings

import requests
import datetime
from tokens import bot_token, weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# from models import UserProfile

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)
    city = str(message.from_user)
    await message.reply("Покажи мені де ти є, а я розкажу що буде")
    print(f"user id is {user_id}")
    print(f"message \n, {city}")


@dp.message_handler()
async def get_weather(message: types.Message):
    # запрос тексту та id
    user_id = str(message.from_user.id)
    first_name = str(message.from_user.first_name)
    last_name = str(message.from_user.last_name)
    city = str(message.from_user)
    # p, _ = UserProfile.objects.get_or_create(
    #     user_id=user_id,
    #     defaults={"user_city": city,
    #               "first_name": first_name,
    #               "last_name": last_name,
    #               }).save()
    code_to_smile = {
        "Clear": "Світить в око \U00002600",
        "Clouds": "Щось якось не дуже, хмарно та безперспективно  \U00002601",
        "Rain": "Воно там мокро сиди в хаті під ковдрою \U00002602",
        "Drizzle": "Воно там мокро сиди в хаті під ковдрою \U00002602",
        "Thunderstorm": "як наєбне блискавкою, то посивієш! \U000026A1",
        "Snow": "Сніг неначе в казці \U00002744",
        "Mist": "Нічого не видно все в тумані \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric"
        )
        data = r.json()

        print(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Не ходи на двір там щось дивне"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Ну шо, ось що тебе чекає за вікном:  \n"
              f"Погода: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Волога: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {wind} м/с\n"
              f"Світає о: {sunrise_timestamp}\nТемніє о: {sunset_timestamp}\nможна виходити без ліхтарика на протязі: {length_of_the_day} год.\n"
              f"*Гарного дня, та краще сиди вдома!"
              )

    except:
        await message.reply("\U00002620 Щось ти не так ввів \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)