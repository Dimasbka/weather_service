# weather_service
простой сервис погоды

## задача 1 
Реализовать API, которое на HTTP-запрос GET /weather?city=<city_name>


Ответ на запрос возвращается объквт формате JSON:
соделжаший три поля 
- `temp` <Число Температура (°C).>, 
- `pressure_mm` <Число   Давление (в мм рт. ст.).>, 
- `wind_speed` <Число Скорость ветра (в м/с).>

Или объкт формате JSON:
содержаший одно поле 
- error <строка: описание ошибки>
и соответстующий код ошибки в заголовке ответа


Пример:
```json
{
    "temp": -4.0, 
    "pressure_mm": 773, 
    "wind_speed": 2.0
}
```


## задача 2
Реализовать телеграмм бота, который после нажатия кнопки "Узнать погоду"
после получения названия города будет присылать прогноз на сегодня

BOT Commands : `/start` отображение начального меню

Пример:
(https://raw.githubusercontent.com/Dimasbka/weather_service/main/bot_screenshot.png)


# Процесс установки и настройки
Установка:
```bash
pip install -r requirements.txt
```

после чего нужно указать свои данные в файле настроек weather_service/settings.py

для базы
- `DATABASES`

кеша
- `CACHES`

настройка апи яндекса
- `YANDEX_API_KEY` укажите свой ключ (можно получить на официальном веб сайте [developer.tech.yandex.ru/services] (https://developer.tech.yandex.ru/services) )
- `YANDEX_API_CACHE_TIME` время кеширования данных 

настройка телеграмм бота 
- `BOT_TOKEN` токен бота (можно получить у [BotFather](https://botostore.com/c/botfather/) )
- `BOT_WEBHOOK` это адрес вашего сайта видимый из веба на который будут приходить сообщения от телеграммана 
- `ALLOWED_HOSTS` - для корректной работы этот же адрес нужно будет добавить в список разрешенныз хостов


Далее нужно  проверить все ли зависимости установились  
```bash
    manage.py check
```
и синхронизировать данные в базе, при миграции добавятся города указанные в ТЗ
```bash
    manage.py makemigrations
    manage.py migrate
```

запуск тестового сервера нужно выполнить команду 
```bash
    manage.py runserver
```


