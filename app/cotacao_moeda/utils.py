import datetime


def iterdates(initial_date, end_date):
    """
    Função para percorrer as datas dentro de um período retornando a data percorrida
    """
    day = datetime.timedelta(days=1)
    current_date = initial_date
    while current_date <= end_date:
        yield current_date
        current_date += day
