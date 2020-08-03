# Generated by Django 3.0.7 on 2020-07-28 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_auto_20200727_1735'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='artwork',
            new_name='innerconsciencemodel',
        ),
        migrations.AlterField(
            model_name='innerconsciencemodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
        migrations.CreateModel(
            name='wanderlustmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('date', models.DateField()),
                ('image', models.FileField(upload_to='portfolio/static/images/uploaded/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series')),
            ],
        ),
        migrations.CreateModel(
            name='thirtyonedaysofmemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('date', models.DateField()),
                ('image', models.FileField(upload_to='portfolio/static/images/uploaded/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series')),
            ],
        ),
        migrations.CreateModel(
            name='theuntoldtruthmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('date', models.DateField()),
                ('image', models.FileField(upload_to='portfolio/static/images/uploaded/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series')),
            ],
        ),
        migrations.CreateModel(
            name='thehumantrapmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('date', models.DateField()),
                ('image', models.FileField(upload_to='portfolio/static/images/uploaded/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series')),
            ],
        ),
        migrations.CreateModel(
            name='soulsearchingmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('date', models.DateField()),
                ('image', models.FileField(upload_to='portfolio/static/images/uploaded/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series')),
            ],
        ),
        migrations.CreateModel(
            name='regenerationmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('date', models.DateField()),
                ('image', models.FileField(upload_to='portfolio/static/images/uploaded/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series')),
            ],
        ),
    ]
