# Generated by Django 3.0.7 on 2020-07-12 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20200712_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
    ]
