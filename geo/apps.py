from django.apps import AppConfig



from django.db.models.signals import post_migrate


class GeoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geo'


    def ready(self):
        from .signals import fill_cities_initial_data
        post_migrate.connect( fill_cities_initial_data, sender=self )



