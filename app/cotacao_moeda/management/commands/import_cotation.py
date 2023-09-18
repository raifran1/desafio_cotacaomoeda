import json
from datetime import datetime

import requests
from django.core.management import BaseCommand

from cotacao_moeda.models import Quotation, QuotationCoin

from moeda.models import Coin


class Command(BaseCommand):
    help = 'Comando para atualizar as taxas de cambio diariamente'

    def handle(self, *args, **kwargs):
        date = datetime.now().date()
        data = requests.get(f'https://api.vatcomply.com/rates?base=USD&date={date}')
        rates = json.loads(data.text)

        coin_base = Coin.objects.get(acronym='USD')

        obj, create = Quotation.objects.get_or_create(
            coin_base=coin_base,
            date=date
        )
        if create:
            for key in rates.get('rates'):
                QuotationCoin.objects.get_or_create(
                    quotation=obj,
                    coin=Coin.objects.get(acronym=key),
                    value=rates.get('rates')[key],
                )


