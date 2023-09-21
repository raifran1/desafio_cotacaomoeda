import requests
from django.test import TestCase

from moeda.models import Coin


class CoinTestCase(TestCase):


    def test_name_coin_method_returns(self):
        coin_obj = Coin(name="Dólar")
        self.assertEqual(str(coin_obj), coin_obj.name)

    def test_api_coin(self):
        response = requests.get('https://cotaon.raifranlucas.dev/api/coins/')
        assert response.status_code == 200
