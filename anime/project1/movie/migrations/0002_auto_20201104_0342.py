# Generated by Django 2.2 on 2020-11-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rilis',
            field=models.DateField(null=True),
        ),
    ]
