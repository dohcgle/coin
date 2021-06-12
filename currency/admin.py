from django.contrib import admin
from currency.models import Currency

@admin.register(Currency)
class Currency(admin.ModelAdmin):
    list_display = ('title', 'description')
    prepopulated_fields = {'slug': ['title']}