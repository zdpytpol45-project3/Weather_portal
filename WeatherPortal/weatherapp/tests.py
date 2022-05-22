import os
import requests

from django.test import TestCase
from django.contrib.auth.models import User
from pprint import pprint

from .models import Location
from. views import get_city_locations
API_KEY = os.getenv('API_KEY')


class TestLocation(TestCase):

    def setUp(self) -> None:
        test_user = User.objects.create(username="sda5", password="sda5@SDA")
        self.client.force_login(test_user)

    def test_can_send_location_information(self):
        """ Test Location model """

        location_data = {
            'name': "Paris",
            "lat": 48.8588897,
            "lon": 	2.3200410217200766,
            "country": "FR",
            "state": "Ile-de-France",
        }

        response = self.client.get("/your-weather/save_location", dict(**location_data))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Location.objects.count(), 1)

    def test_api_response_get_location(self):
        """ Test response from geo api"""
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=9&appid={API_KEY}')

        self.assertTrue(response.ok)

    def test_send_not_exist_location(self):
        """ Test when send not exist location"""
        new_location = get_city_locations('ghhdfgdfg')
        self.assertEqual(new_location, None)

    def test_POST_location_data(self):
        """ Test POST"""
        expected_context = [{'city': 'Paris', 'lat': 48.8588897, 'lon': 2.3200410217200766, 'country': 'FR',
                             'state': 'Ile-de-France', 'number': 0},
                       {'city': 'Paris', 'lat': 48.8566969, 'lon': 2.3514616, 'country': 'FR',
                        'state': 'Ile-de-France', 'number': 1},
                       {'city': 'Paris', 'lat': 33.6617962, 'lon': -95.555513, 'country': 'US',
                        'state': 'Texas', 'number': 2},
                       {'city': 'Paris', 'lat': 38.2097987, 'lon': -84.2529869, 'country': 'US',
                        'state': 'Kentucky', 'number': 3},
                       {'city': 'Paris', 'lat': 48.8588897, 'lon': 2.3200410217200766, 'country': 'FR',
                        'state': 'Ile-de-France', 'number': 4}]
        new_add_city = 'Paris'
        response = self.client.post("/your-weather/", {'name': new_add_city})
        self.assertEqual(response.status_code, 200)
        response_context = response.context['cities_locations']
        self.assertSequenceEqual(response_context, expected_context)