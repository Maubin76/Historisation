from django.db import models

class Personne(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()
    address = models.CharField(max_length=128)