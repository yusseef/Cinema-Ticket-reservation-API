from rest_framework import serializers
from .models import Guest, Movie, Hall, Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['id', 'Hall_num', 'SeatAmount', 'Hall_size', 'hall']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'phone', 'reservation']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        models = Reservation
        fields = ['id', 'reservation']