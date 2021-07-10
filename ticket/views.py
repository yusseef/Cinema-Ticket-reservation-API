from django.http.response import Http404
from django.shortcuts import render
from django.http import JsonResponse
from .models import Guest, Hall, Movie, Reservation
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ReservationSerializer, GuestSerializer, HallSerializer, MovieSerializer
from rest_framework.views import APIView


################ GUEST VIEWS ##################
@api_view(['GET', 'POST'])
def Guest_list(request):
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GuestSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Guest_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########            MOVIES VIEWS ####################3
@api_view(['GET', 'POST'])
def Movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Movies_pk(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Hall_list(request):
    if request.method == 'GET':
        hall = Hall.objects.all()
        serializer = HallSerializer(hall, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = HallSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def Hall_pk(request, pk):
    try:
        hall = Hall.objects.get(pk=pk)
    except hall.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = HallSerializer(hall)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HallSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        hall.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def Reservation_list(request):
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def Reservation_pk(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_200_OK)