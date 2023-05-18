from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('add-income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('credit/', views.credit, name='credit'),
    path('deposit/', views.deposit, name='deposit'),
]
