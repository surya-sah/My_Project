# Generated by Django 4.0.3 on 2022-03-30 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(blank=True, max_length=70, null=True)),
                ('Website', models.CharField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=70, null=True)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(blank=True, max_length=70, null=True)),
                ('Address', models.CharField(blank=True, max_length=70, null=True)),
                ('Phone_number', models.CharField(max_length=12)),
                ('City', models.CharField(blank=True, max_length=200, null=True)),
                ('State', models.CharField(blank=True, max_length=200, null=True)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
