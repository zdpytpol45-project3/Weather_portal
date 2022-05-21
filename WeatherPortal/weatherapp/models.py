from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=35)
    lat = models.DecimalField(max_digits=12, decimal_places=9)
    lon = models.DecimalField(max_digits=12, decimal_places=9)
    country = models.CharField(max_length=5)
    state = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.name} {self.lat} {self.lon} {self.country} {self.state}"

    class Meta:
        verbose_name_plural = 'Locations'