from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class Marker(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True, )
    latitude = models.FloatField(
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
    )
    expire_date = models.DateField(
        default=datetime.now,
        verbose_name="Data Expiração",
    )

    def __str__(self):
        return str(self.name) + " "+str(self.latitude) +" "+ str(self.longitude)+" "+str(self.expire_date)