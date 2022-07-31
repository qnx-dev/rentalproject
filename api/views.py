from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import (
    Rental,
    Reservation,
)
from .serializers import ReservationSerializer

class SeeReservations(APIView):
    def get(self, request):
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


