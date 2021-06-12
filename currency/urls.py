from django.urls import path
from currency.views import currency_list, currency_detail

urlpatterns = [
    path('list/', currency_list, name='currency_list'),
    path('detail/<slug:slug>', currency_detail, name='currency_detail'),

]