# Generated by Django 3.1.7 on 2021-04-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0012_auto_20210408_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealership',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
