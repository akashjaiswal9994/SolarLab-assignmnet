from django.db import models

# Create your models here.

class Country(models.Model):
    flag_link=models.CharField(max_length=500)
    capital=models.CharField(max_length=500)
    largest_city=models.CharField(max_length=400)
    official_languages=models.CharField(max_length=500)
    area_total=models.BigIntegerField
    population=models.CharField(max_length=400)
    GDP_nominal=models.CharField(max_length=500)
    