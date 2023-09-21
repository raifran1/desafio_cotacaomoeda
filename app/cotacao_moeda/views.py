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
        coin_base = Coin.objects.get(acronym='USD')
        time_obj = datetime.datetime.strptime('13:00', '%H:%M')

        obj, create = Quotation.objects.get_or_create(
            coin_base=coin_base,
            date=date,
        )

        update = False
        if not create:
            if obj.time != time_obj:
                obj.time = time_obj
                obj.save()
                update = True

        if create or update:
            data = requests.get(f'https://api.vatcomply.com/rates?base=USD&date={date.date()}')
            rates = json.loads(data.text)

            if not update:
                for key in rates.get('rates'):
                    quotation, create = QuotationCoin.objects.get_or_create(
                        quotation=obj,
                        coin=Coin.objects.get(acronym=key),
                        value=rates.get('rates')[key],
                    )
            else:
                if rates.get('date') == obj.date:
                    for key in rates.get('rates'):
                        try:
                            quotation = QuotationCoin.objects.get(
                                quotation=obj,
                                coin=Coin.objects.get(acronym=key),
                                value=rates.get('rates')[key],
                            )
                            quotation.value = rates.get('rates')[key]
                            quotation.save()
                        except Exception as e:
                            print(e)

    return JsonResponse(data={'detail': 'ok'})
