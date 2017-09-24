from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=20)
    cash = models.DecimalField(default=50000, max_digits=19, decimal_places=2)
    danger = models.IntegerField(default=0)

    on_day = models.OneToOneField(to='Day', on_delete=models.CASCADE)

    def __str__(self):
        return "Name: {}-{}".format(self.name, self.id)


class Day(models.Model):
    day_number = models.IntegerField()
    day_passed = models.BooleanField(default=False)

    def __str__(self):
        return "Day: {}".format(self.day_number)


class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    danger = models.IntegerField(default=0)

    for_sale = models.ForeignKey(to='Day', on_delete=models.CASCADE)

    def __str__(self):
        return "Product: {}".format(self.name)
