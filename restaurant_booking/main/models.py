from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator, validate_email

class Restaurant(models.Model):
    id = models.TextField(primary_key=True)
    rating = models.IntegerField(validators=[
        MaxValueValidator(4),
        MinValueValidator(0)
    ])
    name = models.TextField()
    site = models.TextField(validators=[URLValidator])
    email =  models.TextField(validators=[validate_email])
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()