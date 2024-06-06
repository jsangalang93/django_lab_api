from django.db import models

# Create your models here.
class companies(models.Model):
    name = models.CharField(max_length = 32)
    industry = models.CharField(max_length = 32)

class locations(models.Model):
    street = models.CharField(max_length = 32)
    city = models.CharField(max_length = 32)
    state = models.CharField(max_length = 32)