from django.http import JsonResponse
from django.views import View
from .models import ExchangeRate
from datetime import datetime

class ShowRatesView(View):
    def get(self, request, *args, **kwargs):
        date_str = request.GET.get('date')
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        rates = ExchangeRate.objects.filter(date=date_obj)
        data = {rate.currency.name: str(rate.value) for rate in rates}
        return JsonResponse(data)
