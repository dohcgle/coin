from django.urls import path
from team.views import team

urlpatterns = [
    path('', team, name='team'),

]