from django.shortcuts import render
from currency.models import Currency

def currency_list(request):
    currencies = Currency.objects.all()

    context = {
        "currencies": currencies
    }

    return render(request, 'currency/currency_list.html', context)

def currency_detail(request, slug):
    currency = Currency.objects.get(slug=slug)
    context = {
        "currency": currency
    }
    return render(request, 'currency/currency_detail.html', context)
