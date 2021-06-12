from django.urls import path
from .views import contact, success
urlpatterns = [
    path('', contact, name='contact'),
    path('success/<int:last_id>', success, name='success')
]