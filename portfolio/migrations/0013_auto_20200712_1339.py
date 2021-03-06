# Generated by Django 3.0.7 on 2020-07-12 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20200712_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
    ]
