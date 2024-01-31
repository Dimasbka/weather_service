# Create your tests here.
from django.test import TestCase,  Client
from geo.models import City

class ApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_API_empty_city(self):
        response = self.client.get( "/weather", )
        assert response.status_code == 400

    def test_API_city_not_exists(self):
        response = self.client.get(
                "/weather",
                data={ 'city':'Арканар' },
                headers={' Content-Type':'application/json' },
            )
        assert response.status_code == 404

    def test_API_city_exists(self):
        response = self.client.get(
                "/weather",
                data={ 'city':'Краснодар' },
                headers={' Content-Type':'application/json' },
            )
        assert response.status_code == 200
