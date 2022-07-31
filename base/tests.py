from urllib import response
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from base.models import (Rental,
Reservation,
)

# to run tests execute: python manage.py test <appname> -v 2
class AuthTest(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        Rental.objects.create(name='Rental 1')
        Rental.objects.create(name='Rental 2')

        # Rental 1
        Reservation.objects.create(rental=Rental.objects.get(
            name='Rental 1'),
            checkin = "2022-01-01",
            checkout = "2022-01-13"
            )
        #Rental 1
        Reservation.objects.create(rental=Rental.objects.get(
            name='Rental 1'),
            checkin = "2022-01-20",
            checkout = "2022-02-10"
            )
        #Rental 1
        Reservation.objects.create(rental=Rental.objects.get(
            name='Rental 1'),
            checkin = "2022-02-20",
            checkout = "2022-03-10"
            )

        #Rental 2
        Reservation.objects.create(rental=Rental.objects.get(
            name='Rental 2'),
            checkin = "2022-01-02",
            checkout = "2022-01-20"
            )
        #Rental 2
        Reservation.objects.create(rental=Rental.objects.get(
            name='Rental 2'),
            checkin = "2022-01-20",
            checkout = "2022-02-11"
            )
    
    @classmethod
    def tearDownClass(cls):
        pass

    def test_reservations(self):
        response = self.client.get(reverse('reservations'))
        print (response)
        

        