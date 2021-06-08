
from django.contrib import admin
from django.urls import path, include
from ticket.views import no_rest_no_models, no_rest_models, FBV_list, FBV_pk
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('django/',no_rest_no_models ),
    path('djangomodels/',no_rest_models ),
    path('FBVlist/',FBV_list ),
    path('FBVpk/<str:pk>',FBV_pk ),

]
