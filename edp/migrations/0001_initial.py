# Generated by Django 3.1.7 on 2021-04-26 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DMS', models.FileField(upload_to='')),
                ('Tally', models.FileField(upload_to='')),
                ('ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.salesbooking')),
            ],
        ),
    ]
