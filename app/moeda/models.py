from django.db import models


class Coin(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=150)
    acronym = models.CharField(verbose_name='Sigla', max_length=4, null=True)
    symbol = models.CharField(verbose_name='Simbolo', max_length=4, unique=True)

    class Meta:
        verbose_name = 'Moeda'
        verbose_name_plural = 'Moedas'

    def __str__(self):
        return self.name
