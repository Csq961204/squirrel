from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg

from .models import Squirrel
from .forms import SquirrelForm


def map(request):
    sqs = Squirrel.objects.all()
    return render(request, 'map.html', {'sqs': [{'x': sq.X, 'y': sq.Y} for sq in sqs]})


def sighting_list(request):
    sightings = Squirrel.objects.all()
    return render(request, 'sighting_list.html', {'sightings': sightings, })


def sighting_add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map')
    else:
        form = SquirrelForm()

    context = {'form': form}
    return render(request, 'sighting_add.html', context)


def sighting_update(request, unique_squirrel_id):
    sighting = Squirrel.objects.filter(USID=unique_squirrel_id).first()
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect('sighting_list')
    form = SquirrelForm(instance=sighting)
    return render(request, 'sighting_update.html', {'form': form, 'unique_squirrel_id': unique_squirrel_id})


def sighting_delete(request, unique_squirrel_id):
    sighting = get_object_or_404(Squirrel, USID=unique_squirrel_id)
    sighting.delete()
    return redirect('sighting_list')


def sighting_stats(request):
    lst = []
    lst.append(Squirrel.objects.count())
    lst.append(Squirrel.objects.filter(Age='Adult').count())
    lst.append(Squirrel.objects.filter(Age='Juvenile').count())
    lst.append(Squirrel.objects.aggregate(Avg('X')))
    lst.append(Squirrel.objects.aggregate(Avg('Y')))
    lst.append(Squirrel.objects.filter(PFC='Gray').count())
    lst.append(Squirrel.objects.filter(PFC='Cinnamon').count())
    lst.append(Squirrel.objects.filter(Location='Ground Plane').count())
    lst.append(Squirrel.objects.filter(Location='Above Ground').count())
    lines = [
        'The number of sightings is {}'.format(lst[0]),
        'The number of Adult Squirrel is {}, and the number of Juvenile Squirrel is {}'.format(
        lst[1], lst[2]),
        "The center of all squirrels are {},{}".format(lst[3], lst[4]),
        "There are {:2f} percents of Squirrel with grey primary fur color, and the other {:2f} percents are connamon color".format(
        lst[5] * 100 / (lst[5] + lst[6]), lst[6] * 100 / (lst[5] + lst[6])),
        "There are {:2f} percents of Squirrel above ground, and the other {:2f} are on the ground plane".format(
        lst[8] * 100 / (lst[7] + lst[8]), lst[7] * 100 / (lst[7] + lst[8])),
    ]
    return render(request, 'sighting_stats.html', {'lines': lines})
