# Generated by Django 3.1.7 on 2022-02-06 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lootmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drop',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='日付'),
        ),
    ]
