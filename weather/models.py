from django.db import models

class Forecast(models.Model):
    date = models.DateField()
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()
    wind_speed = models.IntegerField()
    wind_direction = models.CharField(max_length=10)
    rain = models.IntegerField()
