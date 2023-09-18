from django.shortcuts import render

from cotacao_moeda.models import Quotation


def home(request):
    """
    View para renderizar a pagina principal da aplicação, a montagem dos gráficos é realizado via JS e API
    """
    quotations = Quotation.objects.all()[:5]
    return render(request, 'website/home.html', locals())
