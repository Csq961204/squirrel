# Generated by Django 3.0 on 2019-12-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField(null=True)),
                ('Y', models.FloatField(null=True)),
                ('USID', models.CharField(max_length=100, null=True, verbose_name='Unique Squirrel ID')),
                ('Hectare', models.CharField(max_length=100, null=True)),
                ('Shift', models.CharField(max_length=100, null=True)),
                ('Date', models.DateField(null=True)),
                ('HSN', models.IntegerField(null=True, verbose_name='Hectare Squirrel Number')),
                ('Age', models.CharField(max_length=100, null=True)),
                ('PFC', models.CharField(max_length=100, null=True, verbose_name='Primary Fur Color')),
                ('HFC', models.CharField(max_length=100, null=True, verbose_name='Highlight Fur Color')),
                ('CPHC', models.CharField(max_length=100, null=True, verbose_name='Combination of Primary and Highlight Color')),
                ('CN', models.CharField(max_length=100, null=True, verbose_name='Color notes')),
                ('Location', models.CharField(max_length=100, null=True)),
                ('AGSM', models.IntegerField(null=True, verbose_name='Above Ground Sighter Measurement')),
                ('SL', models.CharField(max_length=100, null=True, verbose_name='Specific Location')),
                ('Running', models.BooleanField(null=True)),
                ('Chasing', models.BooleanField(null=True)),
                ('Climbing', models.BooleanField(null=True)),
                ('Eating', models.BooleanField(null=True)),
                ('Foraging', models.BooleanField(null=True)),
                ('OA', models.CharField(max_length=100, null=True, verbose_name='Other Activities')),
                ('Kuks', models.BooleanField(null=True)),
                ('Quaas', models.BooleanField(null=True)),
                ('Moans', models.BooleanField(null=True)),
                ('TF', models.BooleanField(null=True, verbose_name='Tail flags')),
                ('TT', models.BooleanField(null=True, verbose_name='Tail twitches')),
                ('Approaches', models.BooleanField(null=True)),
                ('Indifferent', models.BooleanField(null=True)),
                ('RF', models.BooleanField(null=True, verbose_name='Runs from')),
                ('OI', models.CharField(max_length=100, null=True, verbose_name='Other Interactions')),
                ('LL', models.CharField(max_length=100, null=True, verbose_name='Lat/Long')),
                ('Zip', models.IntegerField(null=True, verbose_name='Zip Codes')),
                ('CD', models.IntegerField(null=True, verbose_name='Community Districts')),
                ('BB', models.IntegerField(null=True, verbose_name='Borough Boundaries')),
                ('CCD', models.IntegerField(null=True, verbose_name='City Council Districts')),
                ('PP', models.IntegerField(null=True, verbose_name='Police Precincts')),
            ],
        ),
    ]
