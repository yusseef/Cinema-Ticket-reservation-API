from rest_framework import serializers
from .models import Guest, Movie, Hall, Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['Hall_num', 'SeatAmount', 'Hall_size', 'movie']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['name', 'phone', 'reservation']

class ReservationSerializer(serializers.ModelSerializer):
    movie_name = serializers.ReadOnlyField(source='movie.name')
    hall_num = serializers.ReadOnlyField(source='hall.Hall_num')
    guest_name = serializers.ReadOnlyField(source='guest.name')
    class Meta:
        model = Reservation
        fields = ['guest_name', 'movie_name', 'hall_num']