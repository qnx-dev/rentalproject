from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.SeeReservations.as_view(), name="reservations"),
]
