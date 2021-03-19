import requests
from celery import chain, shared_task
from home.models import Currency

@shared_task
def parse_private ():
    response =requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    titles=response.json()
    return titles

@shared_task
def get_private (titles):
    Currency.objects.all().delete()
    for title in titles:
        Currency.objects.create(ccy=title['ccy'], base=title['base_ccy'], buy=title['buy'], sale=title['sale'])


@shared_task
def compile_task ():
    chain (
        parse_private.s()
        |
        get_private.s()
    )()