from django.db import models


from django.utils import timezone

class Seats_Data(models.Model):
    totalSeats = models.IntegerField(default=0)
    pricePerSeat = models.FloatField()
    date=models.DateTimeField()


class Users(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    email = models.EmailField()
    password=models.CharField(max_length=20)

    def __unicode__(self):
        return self.id


class My_Booking(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    seats=models.IntegerField(default=0)
    date=models.DateTimeField()
    amount=models.FloatField()
