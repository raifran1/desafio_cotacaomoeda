from django.db import models


class Quotation(models.Model):
    coin_base = models.ForeignKey('moeda.Coin', verbose_name='Moeda Base', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Data', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Cotação'
        verbose_name_plural = 'Cotações'
        ordering = ['-date']

    def __str__(self):
        return f'{self.coin_base.name}'


class QuotationCoin(models.Model):
    quotation = models.ForeignKey('cotacao_moeda.Quotation', on_delete=models.CASCADE, verbose_name='Cotação', null=True)
    coin = models.ForeignKey('moeda.Coin', verbose_name='Moeda', on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Moeda cotação'
        verbose_name_plural = 'Moedas  cotações'

    def __str__(self):
        return self.coin.name
