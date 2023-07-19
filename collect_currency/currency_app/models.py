from django.db import models


class Currency(models.Model):
    char_code = models.CharField(max_length=3, db_index=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering = ['name']



class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, db_index=True)
    date = models.DateField(db_index=True)
    value = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.currency.name} - {self.date}"

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
        unique_together = ('currency', 'date',)
        ordering = ['currency']
