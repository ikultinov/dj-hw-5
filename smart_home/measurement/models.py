from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование')
    description = models.TextField(max_length=50, verbose_name='Описание')

    


class Measurement(models.Model):
    sensor_id = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    temp = models.FloatField(verbose_name='Данные температуры')
    date = models.DateField(auto_now_add=True)
