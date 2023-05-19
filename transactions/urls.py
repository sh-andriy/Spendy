from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_transactions, name='search_transactions'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('delete/<str:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('edit-income/edit/<uuid:transaction_id>/', views.edit_income, name='edit_income'),
    path('edit-expense/edit/<uuid:transaction_id>/', views.edit_expense, name='edit_expense'),
    path('credit/', views.credit, name='credit'),
    path('credit/edit/<uuid:credit_id>/', views.edit_credit, name='edit_credit'),
    path('credit/delete/<uuid:credit_id>/', views.delete_credit, name='delete_credit'),
    path('deposit/', views.deposit, name='deposit'),
    path('deposit/edit/<uuid:deposit_id>/', views.edit_deposit, name='edit_deposit'),
    path('deposit/delete/<uuid:delete_id>/', views.delete_deposit, name='delete_deposit'),
]
