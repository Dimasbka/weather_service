import asyncio

import json

from yaweather import YaWeatherAsync, YaWeather

from django.core.serializers.json import DjangoJSONEncoder
from django.core.cache import cache
from django.conf import settings
from typing import Dict, Tuple, List, Literal, TypeAlias


YANDEX_API_KEY        = getattr( settings, 'YANDEX_API_KEY', False )
YANDEX_API_CACHE_TIME = getattr( settings, 'YANDEX_API_CACHE_TIME', 30*60 )


def get_yandex_weather(city:str, coordinates:Tuple[float, float]):
    """ синхронная версия обновления погоды для бота """

    key = f'weather_{city}'

    #для совместимости со используемым кешем данные хранятся в виде строки 
    data_str = cache.get( key )
    if data_str:
        return json.loads(data_str)

    with YaWeather(api_key=YANDEX_API_KEY, lang='ru_RU',) as y:

        res = y.forecast( coordinates )

        data = {
            'temp':res.fact.temp,               # температура (градусы цельсия)
            'pressure_mm':res.fact.pressure_mm, # атмосферное давление (мм рт.ст.)
            'wind_speed':res.fact.wind_speed,   # скорость ветра (м/с)
        }

        data_str = json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii=False)
        cache.set( key , data_str, YANDEX_API_CACHE_TIME );

        return data


async def get_yandex_weather_async(city: str, coordinates:Tuple[float, float]):
    """ асинхронная версия обновления погоды """

    key = f'weather_{city}'

    #для совместимости со используемым кешем данные хранятся в виде строки 
    data_str = cache.get( key )
    if data_str:
        return json.loads(data_str)

    async with YaWeatherAsync(api_key=YANDEX_API_KEY, lang='ru_RU',) as y:

        res = await y.forecast( coordinates )
        return_data = {
            'temp':res.fact.temp,               # температура
            'pressure_mm':res.fact.pressure_mm, # атмосферное давление
            'wind_speed':res.fact.wind_speed,   # скорость ветра
        }

        # сохраняем данные в кеше сразу в виде строки json
        data_str = json.dumps(return_data, cls=DjangoJSONEncoder, ensure_ascii=False)
        cache.set( key , data_str, YANDEX_API_CACHE_TIME );

        return return_data
