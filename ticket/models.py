import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
#Guest -- Movie -- Hall -- reservation

class Guest(models.Model):
   
    name = models.CharField(max_length=200)
    phone = PhoneNumberField()
    


    def __str__(self):
        return self.name

class Movie(models.Model):
  
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    duration = models.IntegerField()
    start_date = models.TimeField()
    end_date = models.TimeField()
    

    def __str__(self):
        return self.name

class Hall(models.Model):
    
    Hall_num = models.IntegerField()
    SeatAmount = models.IntegerField()
    Hall_size = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name='movie', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.movie, self.Hall_num)


class Reservation(models.Model):
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)

    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, related_name='reservation', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.guest, self.movie, self.hall)