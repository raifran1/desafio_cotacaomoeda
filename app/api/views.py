import datetime

import requests
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response

from cotacao_moeda.models import QuotationCoin
from moeda.models import Coin
from moeda.serializers import CoinSerializer


class QuotationCoinViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        """
        Retornando listagem de cotações baseado nas informações enviadas.
        """
        last_date = datetime.datetime.now() - datetime.timedelta(days=7)

        instances = QuotationCoin.objects.all().order_by('-quotation__date')

        try:
            initial_date = datetime.datetime.strptime(
                request.GET.get('initial_date', str(last_date.date())), '%Y-%m-%d'
            )
            end_date = datetime.datetime.strptime(
                request.GET.get('end_date', str(datetime.datetime.now().date().strftime('%Y-%m-%d'))), '%Y-%m-%d'
            )
        except ValueError:
            return Response({'erro': 'Use o formato AAAA-MM-DD'})

        # vai enviar um get para atualizar o banco de dados
        requests.get(f'{settings.SITE_URL}/update-cotation/?initial_date={initial_date.date()}&end_date={end_date.date()}')

        instances = instances.filter(quotation__date__gte=initial_date)
        instances = instances.filter(quotation__date__lte=end_date)

        list_acronym = request.GET.get('coin_acronym', 'BRL').split(',')

        instances = instances.filter(coin__acronym__in=list_acronym)

        dates = []
        for d in instances:
            if d.quotation.date.strftime('%d/%m') not in dates:
                dates.append(d.quotation.date.strftime('%d/%m'))

        coins = []
        coin_repeat = []
        for c in instances:
            dic = {}
            if c.coin.acronym not in coin_repeat:
                coin_repeat.append(c.coin.acronym)
                dic.update({
                    'acronym': c.coin.acronym,
                    'symbol': c.coin.symbol
                })
                coins.append(dic)

        graphic = []
        for g in coin_repeat:
            for t in instances.filter(coin__acronym=g):
                dic = {}
                dic.update({
                    'coin': g,
                    'data': {
                        'date': t.quotation.date.strftime('%d/%m'),
                        'value': t.value
                    }
                })
                graphic.append(dic)

        data_response = {
            'dates': dates,
            'coins': coins,
            'graphic': graphic
        }
        return Response(data_response)


class CoinsViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        """
        Retornando listagem de moedas para uso no sistema.
        """
        instances = Coin.objects.all()
        serializers = CoinSerializer(instances, many=True)
        return Response(serializers.data)
