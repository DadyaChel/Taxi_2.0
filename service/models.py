from django.db import models
from accounts.models import Profile


class Taxi(models.Model):
    name = models.CharField(max_length=22)
    price = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username} {self.name}'


class Order(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    address = models.CharField(max_length=99)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.taxi.name


class StatusType(models.Model):
    raiting_choice = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    raiting = models.IntegerField(choices=raiting_choice)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.raiting


class StatusDriver(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    point = models.IntegerField()

    def __str__(self):
        return self.name
