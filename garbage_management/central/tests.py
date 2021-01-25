from bottle import view
from django.contrib.auth.models import User, Group
from django.test import RequestFactory, Client
from rest_framework.test import APIRequestFactory
from rest_framework.utils import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Cars, CarType
from rest_framework.test import force_authenticate
from django.test import TestCase


class CarsTests(TestCase):

    def setUp(self):
        # create permissions group
        group_name = "kierownik-przewozu-smieci"
        self.group = Group(name=group_name)
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="kps", email="test@test.com", password="test")
        self.user.groups.add(self.group)
        self.user.save()
        self.client.login(username='kps', password='test')

    def test_create_car(self):
        CarType.objects.create(type="szkło")
        url = '/api/cars'
        data = {
            "car_type": "szkło",
            "number_plate": "Nol 1515",
            "mileage": 2545454,
            "date_oil": "2020-01-15",
            "mileage_oil": 575
        }
        # self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cars.objects.count(), 1)
        self.assertEqual(Cars.objects.get().number_plate, 'Nol 1515')

    def test_get_list_of_cars(self):
        Cars.objects.create(number_plate="Nol 1502")
        url = '/api/cars'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Cars.objects.count(), 1)
        self.assertEqual(Cars.objects.get().number_plate, 'Nol 1502')

    def test_get_car(self):
        Cars.objects.create(number_plate="Nol 1512", mileage=15520, date_oil="2020-01-15", mileage_oil=1450)
        Cars.objects.create(number_plate="Nol 1502")
        url = '/api/cars/2'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, {'id_cars': 2, 'number_plate': 'Nol 1512', "mileage": 15520, "date_oil": "2020-01-15", "mileage_oil": 1450, 'car_type': None})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UsersTests(TestCase):

    def setUp(self):
        # create permissions group
        group_name = "kierownik-przewozu-smieci"
        self.group = Group(name=group_name)
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="kps", email="test@test.com", password="test")

    def test_create_user(self):
        """
        Ensure we can create a new account object.
        """
        self.user.groups.add(self.group)
        self.user.save()
        self.client.login(username='kps', password='test')
        url = '/api/users'
        data = {
            "username": "pracownik",
            "email": "pracownik@gmail.com",
            "first_name": "Pracownik",
            "last_name": "Pracowity",
            "password": "pracownik123"
        }
        # self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)

