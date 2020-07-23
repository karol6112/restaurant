import smtplib
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializers

from restaurant import local_settings


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['date', 'number_of_guests', 'confirmed']

    @action(detail=True)
    def confirm(self, request, **kwargs):
        reservation = self.get_object()
        if reservation.confirmed == False:
            reservation.confirmed = True
            reservation.save()
            # sending infromation
            self.send_message(reservation)
        else:
            raise APIException("The Reservation was confirmed earlier")

        serializer = ReservationSerializers(reservation)
        return Response(serializer.data)

    @action(detail=True)
    def cancel(self, request, **kwargs):
        reservation = self.get_object()
        reservation.confirmed = False
        reservation.save()
        # sending infromation
        self.send_message(reservation)

        serializer = ReservationSerializers(reservation)
        return Response(serializer.data)

    def send_message(self, reservation):
        user = local_settings.EMAIL
        password = local_settings.PASSWORD
        to = user
        # to = reservation.email
        subject = "Reservation"
        confirm_text = f"""Your's reservation has been confirmed.
            Date: {reservation.date}
            Duration:   {reservation.duration}
            Number of guests: {reservation.number_of_guests}                    
            """
        cancel_text = f"""We are sorry but we cannot confirm your reservation.
            Date: {reservation.date}
            Duration:   {reservation.duration}
            Number of guests: {reservation.number_of_guests}                    
            """
        if reservation.confirmed:
            text = confirm_text
        else:
            text = cancel_text

        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(user, password)
            message = f"Subject: {subject} \n\n {text}"
            server.sendmail(user, to, message)
            server.quit()
        except:
            raise APIException("Error")
