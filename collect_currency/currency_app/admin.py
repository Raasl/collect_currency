from django.contrib import admin
from .models import Currency, ExchangeRate

admin.site.register(Currency)


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'value')
    sortable_by = ('currency' ,'value')

