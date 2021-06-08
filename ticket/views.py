from django.shortcuts import render
from django.http import JsonResponse
from .models import Guest, Hall, Movie, Reservation
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ReservationSerializer, GuestSerializer, HallSerializer, MovieSerializer
# Create your views here.
#API without rest or models 
def no_rest_no_models(request):
    guests = [
        {
            'id': 1,
            'name' : 'yussef'

        },
        {
            'id': 2,
            'name' : 'merna'

        },
    ]
    return JsonResponse(guests, safe=False)

#API without rest with models

def no_rest_models(request):
    data = Guest.objects.all()
    movies = Movie.objects.all()
    response = {
        'guests' : list(data.values('name', 'phone')),
        'movies' : list(movies.values())
         
    }
    return JsonResponse(response, safe= False)

@api_view(['GET', 'POST'])
def FBV_list(request):
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
def FBV_pk(request, pk):
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