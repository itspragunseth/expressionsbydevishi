# Generated by Django 3.0.5 on 2020-06-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_paintingdb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paintingdb',
            name='image',
            field=models.ImageField(upload_to='static/portfolio/'),
        ),
    ]
