# Generated by Django 3.2.21 on 2023-09-15 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('moeda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotationCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moeda.coin', verbose_name='Moeda')),
            ],
            options={
                'verbose_name': 'Moeda cotação',
                'verbose_name_plural': 'Moedas  cotações',
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('coin_base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moeda.coin', verbose_name='Moeda Base')),
            ],
            options={
                'verbose_name': 'Cotação',
                'verbose_name_plural': 'Cotações',
            },
        ),
    ]
