import requests
from decimal import Decimal

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import Balance, Transaction, Category


def home(request):
    context = {}
    # if request.user.is_authenticated:
    #     a = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5').json()[0]['buy']
    #     user_balance = Balance.objects.get(user=request.user)
    #     context = {
    #         'home_page': True,
    #         'user_balance': user_balance,
    #         'usd_price': a,
    #     }

    return render(request, 'home.html', context=context)


def add_income(request):

    if request.method == 'POST':
        category_id = request.POST['income_category']
        amount = Decimal(request.POST['income_amount'])
        user_balance = Balance.objects.get(user=request.user)

        transaction = Transaction(
            balance=user_balance,
            category=Category.objects.get(id=category_id),
            amount=amount,
        )
        transaction.save()

        user_balance.amount += transaction.amount
        user_balance.save()

        return redirect('transactions:home')

    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }

    return render(request, 'transactions/add_income.html', context=context)


def add_expense(request):

    if request.method == 'POST':
        category_id = request.POST['expense_category']
        amount = Decimal(request.POST['expense_amount'])
        user_balance = Balance.objects.get(user=request.user)

        transaction = Transaction(
            balance=user_balance,
            category=Category.objects.get(id=category_id),
            amount=amount,
        )
        transaction.save()

        user_balance.amount -= transaction.amount
        user_balance.save()

        return redirect('transactions:home')

    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }

    return render(request, 'transactions/add_expense.html', context=context)


def credit(request):
    return render(request, 'transactions/credit_deposit/credit.html')


def deposit(request):
    return render(request, 'transactions/credit_deposit/deposit.html')
