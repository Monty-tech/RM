# Generated by Django 3.1.7 on 2021-04-08 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesbooking',
            old_name='Acc',
            new_name='ACC',
        ),
        migrations.RenameField(
            model_name='salesbooking',
            old_name='Amc',
            new_name='Annual_Maintance_Cost',
        ),
        migrations.RenameField(
            model_name='salesbooking',
            old_name='FASTag',
            new_name='FASTAG',
        ),
        migrations.RenameField(
            model_name='salesbooking',
            old_name='Ins_AMT',
            new_name='Insurance_AMT',
        ),
        migrations.RenameField(
            model_name='salesbooking',
            old_name='Rto',
            new_name='RTO',
        ),
        migrations.RenameField(
            model_name='salesbooking',
            old_name='Tcs',
            new_name='TCS',
        ),
        migrations.RenameField(
            model_name='salesbooking',
            old_name='Total',
            new_name='TOTAL',
        ),
    ]
