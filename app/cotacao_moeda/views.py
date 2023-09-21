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

    # organiza todas as datas de dias util do período em uma lista
    dates = []
    for day in iterdates(initial_date, end_date):
        if day.weekday() not in (5, 6):
            dates.append(day)

    # itera e inicia o cadastro
    for date in dates:
        coin_base = Coin.objects.get(acronym='USD')
        # foi utilizado um padrão de forçar a atualização quando não estiver marcado como sincronizado antes
        #Percepção de que a API tem um atraso de atualização
        time_now = datetime.datetime.now().time()

        # armazena ou cria o obj
        obj, create = Quotation.objects.get_or_create(
            coin_base=coin_base,
            date=date,
        )

        # gerencia o padrão de update, se não tiver marcado como finalizado ou tiver com limite de horario para finalizar
        update = False
        if not create:
            if not obj.sinc:
                obj.time = time_now
                obj.save()
                update = True

        # se obj for criado ou atualizado ele vai puxar as cotações das moedas
        if create or update:
            data = requests.get(f'https://api.vatcomply.com/rates?base=USD&date={date.date()}')
            rates = json.loads(data.text)

            # caso o obj esteja sendo criado, ele cria as taxas de conversão
            if not update:
                for key in rates.get('rates'):
                    QuotationCoin.objects.get_or_create(
                        quotation=obj,
                        coin=Coin.objects.get(acronym=key),
                        value=rates.get('rates')[key],
                    )
            else:
                # caso contrario valida se a data enviada é a mesma que esta iterando, se for e ainda não tiver marcada
                #como finalizada ele vai atualizar
                if rates.get('date') == str(obj.date):
                    if not obj.sinc:
                        obj.sinc = True
                        obj.save()
                        for key in rates.get('rates'):
                            try:
                                quotation = QuotationCoin.objects.get(
                                    quotation=obj,
                                    coin=Coin.objects.get(acronym=key),
                                )
                                quotation.value = rates.get('rates')[key]
                                quotation.save()
                            except Exception as e:
                                print(e)

    return JsonResponse(data={'detail': 'ok'})
