# Generated by Django 3.0.7 on 2020-07-12 17:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20200712_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
    ]
