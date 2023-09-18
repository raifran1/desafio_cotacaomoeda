from django.contrib import admin
from .models import Quotation, QuotationCoin


class QuotationCoinInline(admin.TabularInline):
    model = QuotationCoin


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    inlines = [QuotationCoinInline]
    list_display = ['__str__', 'date']
