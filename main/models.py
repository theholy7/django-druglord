from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=20)
    cash = models.DecimalField(max_digits=19, decimal_places=2)
    danger = models.IntegerField()


class Day(models.Model):
    day_number = models.IntegerField(name="Day")


class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    danger = models.IntegerField()
