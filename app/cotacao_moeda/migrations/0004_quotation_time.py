# Generated by Django 3.2.21 on 2023-09-21 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao_moeda', '0003_auto_20230918_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
