from django.urls import path
from .views import incoming_data

urlpatterns = [
    path('incoming_data/', incoming_data, name='incoming_data'),
]
