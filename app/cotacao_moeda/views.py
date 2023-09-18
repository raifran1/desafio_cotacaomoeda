import json
import datetime
import requests
from django.http import JsonResponse

from moeda.models import Coin
from .models import Quotation, QuotationCoin
from .utils import iterdates


def update_coins_cotation(request):
    """
    Essa view serve para puxar os dados atualizados de um período e persistir em banco de dados
    Utilização: via JS durante o uso de um filtro personalizado
    """
    initial_date = datetime.datetime.strptime(
        request.GET.get('initial_date', str(datetime.datetime.now().date().strftime('%Y-%m-%d'))), '%Y-%m-%d'
    )
    end_date = datetime.datetime.strptime(
        request.GET.get('end_date', str(datetime.datetime.now().date().strftime('%Y-%m-%d'))), '%Y-%m-%d'
    )

    dates = []
    for day in iterdates(initial_date, end_date):
        if day.weekday() not in (5, 6):
            dates.append(day)

    for date in dates:
        data = requests.get(f'https://api.vatcomply.com/rates?base=USD&date={date.date()}')
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

    return JsonResponse(data={'detail': 'ok'})
