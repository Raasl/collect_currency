import requests
from django.core.management.base import BaseCommand
from currency_app.models import Currency, ExchangeRate
from datetime import date

class Command(BaseCommand):
    help = 'Скачать курсы обмена с cbr-xml-daily.ru'

    def handle(self, *args, **kwargs):
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()
        for key, value in data['Valute'].items():
            currency, created = Currency.objects.get_or_create(
                char_code=value['CharCode'],
                defaults={'name': value['Name']},
            )
            ExchangeRate.objects.update_or_create(
                currency=currency,
                date=date.today(),
                defaults={'value': value['Value']},
            )
        self.stdout.write(self.style.SUCCESS('Успешно обновлены курсы валют'))
