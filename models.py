from django.db import models
import json

class GeoName(models.Model):
    name = models.CharField(max_length=100)
    geogcode=models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"Name: {self.name} Geogcode: {self.geogcode}"

class GeoData(models.Model):
    year = models.IntegerField()
    age = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    geo_name = models.ForeignKey(GeoName, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"Geography: {self.geo_name} Year: {self.year} Age: {self.age} Male:{self.male} Female:{self.female}"