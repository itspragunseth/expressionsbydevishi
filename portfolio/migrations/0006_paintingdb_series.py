# Generated by Django 3.0.7 on 2020-07-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200706_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='paintingdb',
            name='series',
            field=models.PositiveSmallIntegerField(choices=[(1, 'None'), (2, 'Test Series'), (3, 'Test 2 Series')], default=1),
        ),
    ]
