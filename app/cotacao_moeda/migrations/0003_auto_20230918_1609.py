# Generated by Django 3.2.21 on 2023-09-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao_moeda', '0002_quotationcoin_quotation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotation',
            options={'ordering': ['-date'], 'verbose_name': 'Cotação', 'verbose_name_plural': 'Cotações'},
        ),
        migrations.AlterField(
            model_name='quotationcoin',
            name='value',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Valor'),
        ),
    ]