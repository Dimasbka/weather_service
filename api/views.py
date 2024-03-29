import asyncio
import json

from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core.cache import cache

from geo.models import City
from geo.yandex_weather import get_yandex_weather_async


# классы для корректной работы с руским языком в json 
class UTF8JsonResponse(JsonResponse):
    def __init__(self, *args, json_dumps_params=None, **kwargs):
        json_dumps_params = {"ensure_ascii": False, **(json_dumps_params or {})}
        super().__init__(*args, json_dumps_params=json_dumps_params, **kwargs)

class JsonResponseBadRequest(UTF8JsonResponse):
    status_code = 400

class JsonResponseNotFound(UTF8JsonResponse):
    status_code = 404


class CityWeather(View):
    http_method_names = [
        "get",
    ]

    async def get(self, request, *args, **kwargs):
        if ('city' not in request.GET) or (request.GET['city']==''):
            return JsonResponseBadRequest({
                'error':"Не передан обязательный параметр 'city'"
            })

        city_name = request.GET['city']

        city = await City.objects.filter( name__iexact=city_name ).afirst()

        if city == None:
            return JsonResponseNotFound({
                'error':f"Город '{city}' не найден"
            })

        data = await get_yandex_weather_async( (city.latitude, city.longitude) )

        return JsonResponse(data)