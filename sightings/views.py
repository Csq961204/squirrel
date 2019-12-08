from django.shortcuts import render

from .models import Squirrel


def map(request):
    sqs = Squirrel.objects.all()
    return render(request, 'map.html', {'sqs': [{'x': sq.X, 'y': sq.Y} for sq in sqs]})
