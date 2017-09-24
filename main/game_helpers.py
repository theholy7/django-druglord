"""
Game helper functions
"""

import random

from . import models, settings


def create_game_day(day_number):

    day = models.Day(day_number=day_number)
    day.save()

    for drug in settings.DRUGS.keys():

        price = settings.DRUGS[drug]['BASE_PRICE']
        quantity = settings.DRUGS[drug]['BASE_QUANTITY']
        danger = settings.DRUGS[drug]['BASE_DANGER']

        p = models.Product(name=drug,
                           price=price,
                           quantity=quantity,
                           danger=danger,
                           for_sale=day)
        p.save()

    return day
