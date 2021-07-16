
from django.contrib import admin
from django.urls import path, include
from ticket.views import Guest_list, Guest_pk, Movies_list, Movies_pk, Hall_list, Hall_pk, Reservation_list, Reservation_pk, find_guest, find_movie, find_guest
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('guestlist/',Guest_list ),
    path('guestpk/<str:pk>',Guest_pk ),
    path('movieslist/', Movies_list),
    path('moviespk/<str:pk>',Movies_pk ),
    path('halllist/', Hall_list),
    path('hallpk/<str:pk>',Hall_pk ),
    path('reservationlist/', Reservation_list),
    path('reservationpk/<str:pk>',Reservation_pk ),
    path('findmovie/', find_movie),
 
    path('findguest/', find_guest),
   
   
]
