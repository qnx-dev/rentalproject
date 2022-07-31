from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import (
    Rental,
    Reservation,
)
from .serializers import ReservationSerializer

class SeeReservations(APIView):
    def get(self, request):
        populateData()
        dataset = []
        query = Reservation.objects.all().values(
            'rental__name',
            'id',
            'checkin',
            'checkout',
        )
        # <QuerySet [{'rental__name': 'Rental 1', 'id': 2, 'checkin': datetime.date(2022, 1, 1), 'checkout': datetime.date(2022, 1, 13)}, 

        for data in query:
            prev_issue = (Reservation.objects
            .values('id')
            .filter(rental__name=data.get('rental__name'), id__lt=data.get('id'))
            .order_by('-id')
            .first())
            dataset.append(data)
            dataset.append({"previous reservation, ID ": prev_issue})

        res = {
            'data' : dataset
        }

        return Response(res)


def populateData():
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
