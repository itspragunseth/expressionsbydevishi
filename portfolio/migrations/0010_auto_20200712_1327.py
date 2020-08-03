# Generated by Django 3.0.7 on 2020-07-12 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20200707_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='artwork',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Series'),
        ),
    ]
