from .models import City
import re



def fill_cities_initial_data(**kwargs):
    """
        Сигнал вызывается после миграции 

        и если таблица городов пустая загружает в базу города из файла 
        в файле обрабатываются строки вида 
             Абакан — 53.72, 91.43
             Адлер — 43.43, 39.92
        остальные игнорируются
    """

    if City.objects.exists():
        return

    with open('geo/data/city.txt', 'r', encoding='utf-8' ) as f:
        i = 0
        for line in f:
            m = re.search( '(?P<name>.*?) — (?P<lat>(\-?|\+?)?\d+(\.\d+)?),\s*(?P<long>(\-?|\+?)?\d+(\.\d+)?)', line , re.UNICODE )
            if m:
                name, latitude, longitude = m.group( 'name', 'lat', 'long' )
                City( name=name, latitude=latitude, longitude=longitude ).save()
                i += 1
            else:
                continue

    print(f' {i} initial cities added')

