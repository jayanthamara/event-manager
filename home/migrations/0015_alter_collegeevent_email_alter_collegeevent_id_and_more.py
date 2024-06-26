# Generated by Django 5.0.1 on 2024-04-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20221020_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeevent',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='collegeevent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='eventadvisor',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='eventadvisor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='partiesevent',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='partiesevent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='technicalevent',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='technicalevent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='weddingevent',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='weddingevent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
