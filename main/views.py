import logging

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . import game_helpers, models

logger = logging.getLogger(__name__)


# Create your views here.


def home(request):
    chars = models.Character.objects.all()

    context = {'characters': chars}

    return render(request, 'main/home.html', context=context)


def day(request, char_id, day_number):
    try:
        day_number = int(day_number)
    except ValueError as e:
        logger.error("Error with day_number: {}".format(e))

    char = get_object_or_404(models.Character, pk=char_id)

    day = game_helpers.create_game_day(day_number)

    context = {
        "char": char,
        "day": day,
        "next_day": day.day_number + 1
    }

    return render(request, 'main/day.html', context=context)
