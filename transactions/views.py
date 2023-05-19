import requests
from decimal import Decimal

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import Balance, Transaction, Category, CreditDeposit


def home(request):
    context = {}
    if request.user.is_authenticated:

        user_balance = Balance.objects.get(user=request.user)
        transactions = Transaction.objects.filter(balance=user_balance)
        context = {
            'home_page': True,
            'transactions': transactions,
        }

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
    user_balance = Balance.objects.get(user=request.user)
    if request.method == 'POST':
        amount = request.POST['credit_amount']
        payment = request.POST['credit_payment']
        profit = request.POST['credit_profit']

        credit = CreditDeposit(
            balance=user_balance,
            amount=amount,
            income=payment,
            profit=profit,
            percentage=7.0,
        )
        credit.save()

        messages.success(request, "Credit Added Successfully 👾!")
        return redirect('transactions:home')

    credits = CreditDeposit.objects.filter(balance=user_balance)

    context = {
        'credits': credits
    }

    return render(request, 'transactions/credit_deposit/credit.html', context=context)


def deposit(request):
    if request.method == 'POST':
        amount = request.POST['deposit_amount']
        income = request.POST['deposit_income']
        profit = request.POST['deposit_profit']

        deposits = CreditDeposit(
            balance=Balance.objects.get(user=request.user),
            amount=amount,
            income=income,
            profit=profit,
            percentage=11.5,
        )
        deposits.save()

        messages.success(request, "Deposit Added Successfully 👾!")
        return redirect('transactions:home')

    context = {}
    return render(request, 'transactions/credit_deposit/deposit.html', context=context)
