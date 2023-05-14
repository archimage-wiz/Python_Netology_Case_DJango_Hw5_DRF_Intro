from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=4096)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    mes_temperature = models.FloatField(null=False)
    mes_time = models.DateField(auto_now_add=True)
    
