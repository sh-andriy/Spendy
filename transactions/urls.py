from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('add-income/', views.add_income, name='add_income'),
]
