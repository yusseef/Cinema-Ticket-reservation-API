from django.contrib import admin
from .models import Guest, Movie, Hall, reservation
# Register your models here.
models = [Guest, Movie, Hall, reservation]
admin.site.register(models)