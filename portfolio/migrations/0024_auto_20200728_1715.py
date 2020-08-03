# Generated by Django 3.0.7 on 2020-07-28 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_auto_20200728_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innerconsciencemodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
        migrations.AlterField(
            model_name='regenerationmodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
        migrations.AlterField(
            model_name='soulsearchingmodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
        migrations.AlterField(
            model_name='thehumantrapmodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
        migrations.AlterField(
            model_name='theuntoldtruthmodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
        migrations.AlterField(
            model_name='thirtyonedaysofmemodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
        migrations.AlterField(
            model_name='wanderlustmodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
    ]
