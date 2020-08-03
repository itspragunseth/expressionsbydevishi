# Generated by Django 3.0.7 on 2020-07-12 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20200712_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
    ]
