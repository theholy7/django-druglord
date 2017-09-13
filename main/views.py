from django.shortcuts import render

from . import models

# Create your views here.


def home(request):
    chars = models.Character.objects.all()

    context = {'characters': chars}

    return render(request, 'main/home.html', context=context)


def day(request, id, day):
    pass
