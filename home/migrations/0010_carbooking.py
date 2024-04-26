# Generated by Django 4.1.1 on 2022-10-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_driverbookingcar'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('model', models.CharField(max_length=50)),
                ('pickup', models.CharField(max_length=122)),
                ('destination', models.CharField(max_length=122)),
                ('pickdate', models.DateField(null=True)),
                ('pickuptime', models.TimeField(null=True)),
                ('dropdate', models.DateField(null=True)),
                ('droptime', models.TimeField(null=True)),
            ],
        ),
    ]