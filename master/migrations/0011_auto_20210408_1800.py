# Generated by Django 3.1.7 on 2021-04-08 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0010_auto_20210408_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealbreakup',
            old_name='acc',
            new_name='ACC',
        ),
        migrations.RenameField(
            model_name='dealbreakup',
            old_name='amc',
            new_name='Annual_Maintance_Cost',
        ),
        migrations.RenameField(
            model_name='dealbreakup',
            old_name='fASTag',
            new_name='FASTAG',
        ),
        migrations.RenameField(
            model_name='dealbreakup',
            old_name='ins_AMT',
            new_name='Insurance_Amount',
        ),
        migrations.RenameField(
            model_name='dealbreakup',
            old_name='rto',
            new_name='RTO',
        ),
        migrations.RenameField(
            model_name='dealbreakup',
            old_name='tcs',
            new_name='TCS',
        ),
        migrations.RenameField(
            model_name='dealbreakup',
            old_name='total',
            new_name='TOTAL',
        ),
    ]