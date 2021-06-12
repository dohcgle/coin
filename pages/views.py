from django.shortcuts import render
from currency.models import Currency
from team.models import Team


def home(request):
    currencies = Currency.objects.order_by('-created_at').all()[:3]
    teams = Team.objects.all()[:3]
    context = {
        "currencies": currencies,
        "teams": teams
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')
