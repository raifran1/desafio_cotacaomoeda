import json

import requests
from django.test import TestCase

from moeda.models import Coin


class QuotationTestCase(TestCase):

    def test_api_quotation(self):
        response = requests.get('https://cotaon.raifranlucas.dev/api/quotationcoin-graphic/')
        assert response.status_code == 200

    def test_api_quotation_with_initial_date(self):
        formats = ['2020-30-03', '2020-03-03', '20-03-2023', '20-2023-03']
        for i in formats:
            response = requests.get(f'https://cotaon.raifranlucas.dev/api/quotationcoin-graphic/?initial_date={i}')
            try:
                assert response.status_code == 200
            except:
                assert response.status_code == 400 and json.loads(response.text).get('erro') == 'Use o formato AAAA-MM-DD'

    def test_api_quotation_with_end_date(self):
        formats = ['2020-30-03', '2020-03-03', '20-03-2023', '20-2023-03']
        for i in formats:
            response = requests.get(f'https://cotaon.raifranlucas.dev/api/quotationcoin-graphic/?initial_date={i}')
            try:
                assert response.status_code == 200
            except:
                assert response.status_code == 400 and json.loads(response.text).get('erro') == 'Use o formato AAAA-MM-DD'

    def test_api_quotation_with_end_date_less_then_initial_date(self):
        initial_date = ['2020-30-03', '2020-05-03', '20-03-2023', '22-2023-03']
        end_date = ['2020-31-03', '2020-03-03', '20-03-2023', '20-2023-03']
        for i in range(0, len(initial_date)):
            response = requests.get(f'https://cotaon.raifranlucas.dev/api/quotationcoin-graphic/?initial_date={initial_date[i]}&end_date={end_date[i]}')
            try:
                assert response.status_code == 200
            except:
                assert response.status_code == 400 and json.loads(response.text).get(
                    'erro') in ['Use o formato AAAA-MM-DD', 'A data inicial informada deve ser menor que a data final']

    def test_api_quotation_with_coin(self):
        coins = ['BRL', 'GPP', 'EUR,JYP', 'USD_BRL', 'EUR-BRL', '']
        for c in coins:
            response = requests.get(f'https://cotaon.raifranlucas.dev/api/quotationcoin-graphic/?coin={c}')
            assert response.status_code == 200
