from moeda.serializers import CoinSerializer
from .models import Quotation, QuotationCoin
from rest_framework import serializers


class QuotationSerializer(serializers.ModelSerializer):
    coin_base = CoinSerializer()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Quotation
        fields = (
            'coin_base',
            'date'
        )

    def get_date(self, obj):
        return obj.date.strftime('%d/%m')


class QuotationCoinSerializer(serializers.ModelSerializer):
    quotation = QuotationSerializer()
    coin = CoinSerializer()

    class Meta:
        model = QuotationCoin
        fields = (
            'quotation',
            'coin',
            'value'
        )
