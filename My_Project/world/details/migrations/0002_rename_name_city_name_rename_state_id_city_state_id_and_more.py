# Generated by Django 4.0.4 on 2022-04-14 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='State_id',
            new_name='state_id',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Phone_code',
            new_name='phoneCode',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Sortname',
            new_name='sortname',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='Country_id',
            new_name='country_id',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='Name',
            new_name='name',
        ),
    ]
