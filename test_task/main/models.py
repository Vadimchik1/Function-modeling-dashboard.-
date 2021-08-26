from django.db import models
from django.db.models import Model, CharField, IntegerField, ImageField, DateTimeField


# Create your models here.

class Function(Model):
    formula = CharField(max_length=20)
    interval = IntegerField()
    picture = ImageField(upload_to="pictures/%Y/%m/%d/", null=True)
    step = IntegerField()
    date_of_processing = DateTimeField(null=True)
