
from django.contrib import admin
from django.urls import path,include

from api.views import CityWeather

urlpatterns = [
    path('weather', CityWeather.as_view() ),
    path('admin/', admin.site.urls),
    path('', include('bot.urls')),
]
