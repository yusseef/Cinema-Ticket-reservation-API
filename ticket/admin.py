from django.contrib import admin
from .models import Guest, Movie, Hall, Reservation
# Register your models here.
models = [Guest, Movie, Hall, Reservation]
admin.site.register(models)