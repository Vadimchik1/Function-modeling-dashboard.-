from django.db import models
from django.db.models import Model, CharField, IntegerField, ImageField, DateTimeField, BinaryField


# Create your models here.

class Function(Model):
    class Meta:
        verbose_name = 'Функции'
        verbose_name_plural = 'Функции'
    formula = CharField(max_length=20, verbose_name='Функция')
    interval = IntegerField(verbose_name='Интервал')
    picture = ImageField(upload_to="pictures/%Y/%m/%d/", null=True, verbose_name='График')
    step = IntegerField(verbose_name='Шаг')
    date_of_processing = DateTimeField(null=True, verbose_name='Дата обработки')
