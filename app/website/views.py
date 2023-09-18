from django.shortcuts import render


def home(request):
    """
    View para renderizar a pagina principal da aplicação, retornando dados necessários para visualização e construção
    dos gráficos.
    """
    return render(request, 'website/home.html', locals())
