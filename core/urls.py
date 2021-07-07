
from django.contrib import admin
from django.urls import path, include
from ticket.views import Guest_list, Guest_pk, Movies_list, Movies_pk
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('Guestlist/',Guest_list ),
    path('Guestpk/<str:pk>',Guest_pk ),
    path('movieslist/', Movies_list),
    path('moviespk/<str:pk>',Movies_pk ),
   
]
