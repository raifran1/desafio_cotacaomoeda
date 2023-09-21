# Generated by Django 3.2.21 on 2023-09-21 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao_moeda', '0004_quotation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='sinc',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='time',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Última atualização'),
        ),
    ]