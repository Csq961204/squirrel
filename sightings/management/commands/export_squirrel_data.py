from django.core.management.base import BaseCommand

import csv

from sightings.models import Squirrel


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='/path/to/file.csv')

    def handle(self, *args, **options):
        header = "X,Y,Unique Squirrel ID,Hectare,Shift,Date,Hectare Squirrel Number,Age,Primary Fur Color,Highlight " \
                 "Fur Color,Combination of Primary and Highlight Color,Color notes,Location,Above Ground Sighter " \
                 "Measurement,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas," \
                 "Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs from,Other Interactions,Lat/Long," \
                 "Zip Codes,Community Districts,Borough Boundaries,City Council Districts,Police Precincts\n "
        with open(options['file_path'], 'w') as f:
            f.write(header)
            for s in Squirrel.objects.all():
                f.write(str(s) + "\n")
