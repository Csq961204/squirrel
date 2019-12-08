from django.core.management.base import BaseCommand

import csv

from sightings.models import Squirrel


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='/path/to/file.csv')

    def handle(self, *args, **options):
        with open(options['file_path']) as f:
            pass
            reader = csv.reader(f)
            # skip header
            next(reader)
            for row in reader:
                Squirrel.objects.create_squirrel(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
                    row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33],
                    row[34], row[35]
                )