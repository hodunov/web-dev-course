# Generated by Django 3.1.7 on 2021-04-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210325_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(default=14),
        ),
    ]
