# Generated by Django 3.1.7 on 2022-02-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lootmanage', '0004_remove_drop_hope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='getBody',
            field=models.IntegerField(default=0, verbose_name='胴取得数'),
        ),
    ]
