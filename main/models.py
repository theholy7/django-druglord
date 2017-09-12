from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=20)
    cash = models.DecimalField(max_digits=19, decimal_places=2)
    danger = models.IntegerField()

    on_day = models.OneToOneField(to='Day', on_delete=models.CASCADE)


class Day(models.Model):
    day_number = models.IntegerField(name="Day")


class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    danger = models.IntegerField(default=0)

    for_sale = models.ForeignKey(to='Product', on_delete=models.CASCADE)
