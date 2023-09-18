import json

import requests
from django.core.management import BaseCommand

from moeda.models import Coin


class Command(BaseCommand):
    help = 'Comando para cadastrar as moedas Euro, Dollar e Yene'

    def handle(self, *args, **kwargs):
        data = requests.get('https://api.vatcomply.com/currencies')
        coins_database = json.loads(data.text)

        for key in coins_database:
            coin = coins_database[key]
            Coin.objects.get_or_create(
                name=coin.get('name'),
                acronym=coin.get('symbol')
            )
