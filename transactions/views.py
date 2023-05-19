import requests
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, date

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


@login_required
def search_transactions(request):
    from_date_str = request.GET.get('from_date')
    to_date_str = request.GET.get('to_date')

    if from_date_str or to_date_str:
        transactions = Transaction.objects.all()

        if from_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date()
            transactions = transactions.filter(created_at__date__gte=from_date)

        if to_date_str:
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date()
            transactions = transactions.filter(created_at__date__lte=to_date)

        transactions = transactions.order_by('created_at')

        context = {
            'transactions': transactions,
        }
        messages.success(request, "Search went successfully! 🥳")
        return render(request, 'home.html', context)

    messages.error(request, "Sorry, from_date or to_date is not provided >_<")
    return redirect('transactions:home')


@login_required
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

        messages.success(request, "Transaction Added Successfully ⭐️")
        return redirect('transactions:home')

    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }

    return render(request, 'transactions/add_income.html', context=context)


@login_required
def edit_income(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    categories = Category.objects.order_by('name')

    if request.method == 'POST':
        category_id = request.POST['income_category']
        amount = Decimal(request.POST['income_amount'])

        user_balance = transaction.balance
        user_balance.amount -= transaction.amount  # Deduct the previous income amount

        transaction.category = Category.objects.get(id=category_id)
        transaction.amount = amount

        user_balance.amount += amount  # Add the updated income amount
        user_balance.save()
        transaction.save()

        messages.success(request, "Transaction Edited Successfully ⭐️")

        return redirect('transactions:home')

    context = {
        'transaction': transaction,
        'categories': categories,
    }


    return render(request, 'transactions/edit_income.html', context=context)


@login_required
def edit_expense(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    categories = Category.objects.order_by('name')

    if request.method == 'POST':
        category_id = request.POST['expense_category']
        amount = Decimal(request.POST['expense_amount'])

        user_balance = transaction.balance
        user_balance.amount += transaction.amount  # Add back the previous expense amount

        transaction.category = Category.objects.get(id=category_id)
        transaction.amount = amount

        user_balance.amount -= amount  # Deduct the updated expense amount
        user_balance.save()
        transaction.save()

        messages.success(request, "Transaction Edited Successfully ⭐️")
        return redirect('transactions:home')

    context = {
        'transaction': transaction,
        'categories': categories,
    }


    return render(request, 'transactions/edit_expense.html', context=context)


@login_required
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

        messages.success(request, "Transaction Added Successfully ⭐️")
        return redirect('transactions:home')

    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }

    return render(request, 'transactions/add_expense.html', context=context)


@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.delete()

    messages.success(request, "Transaction Deleted Successfully 😎")
    return redirect('transactions:home')


@login_required
def credit(request):
    if request.method == 'POST':
        amount = request.POST.get('credit_amount', 0)
        income = request.POST.get('credit_income', 0)
        loss = request.POST.get('credit_loss', 0)

        credit = CreditDeposit(
            balance=Balance.objects.get(user=request.user),
            amount=amount,
            income=income,
            profit=loss,
            percentage=13.9,
        )
        credit.save()

        messages.success(request, "Credit Added Successfully 👾!")
        return redirect('transactions:credit')

    credits = CreditDeposit.objects.filter(balance__user=request.user)

    context = {
        'credits': credits
    }

    return render(request, 'transactions/credit_deposit/credit.html', context=context)


@login_required
def edit_credit(request, credit_id):
    credit = get_object_or_404(CreditDeposit, id=credit_id)

    if request.method == 'POST':
        amount = request.POST.get('credit_amount', 0)
        income = request.POST.get('credit_income', 0)
        loss = request.POST.get('credit_loss', 0)

        credit.amount = amount
        credit.income = income
        credit.profit = loss
        credit.save()

        messages.success(request, "Credit Updated Successfully 👾!")
        return redirect('transactions:credit')

    context = {
        'credit': credit
    }

    return render(request, 'transactions/credit_deposit/edit_credit.html', context=context)


@login_required
def delete_credit(request, credit_id):
    if request.method == 'GET':
        credit = get_object_or_404(CreditDeposit, id=credit_id)
        credit.delete()
        messages.success(request, "Transaction Deleted Successfully 👾!")
    return redirect('transactions:credit')


@login_required
def deposit(request):
    if request.method == 'POST':
        amount = request.POST['deposit_amount']
        income = request.POST['deposit_income']
        profit = request.POST['deposit_profit']

        deposit = CreditDeposit(
            balance=Balance.objects.get(user=request.user),
            amount=amount,
            income=income,
            profit=profit,
            percentage=11.5,
        )
        deposit.save()

        messages.success(request, "Deposit Added Successfully 👾!")

    deposits = CreditDeposit.objects.filter(balance__user=request.user)

    context = {
        'deposits': deposits
    }

    return render(request, 'transactions/credit_deposit/deposit.html', context=context)


@login_required
def edit_deposit(request, deposit_id):
    deposit = get_object_or_404(CreditDeposit, id=deposit_id)

    if request.method == 'POST':
        amount = request.POST['deposit_amount']
        income = request.POST['deposit_income']
        profit = request.POST['deposit_profit']

        deposit.amount = amount
        deposit.income = income
        deposit.profit = profit
        deposit.save()

        messages.success(request, "Deposit Updated Successfully 👾!")
        return redirect('transactions:deposit')

    context = {
        'deposit': deposit
    }

    return render(request, 'transactions/credit_deposit/edit_deposit.html', context=context)


@login_required
def delete_deposit(request, delete_id):
    if request.method == 'GET':
        deposit = CreditDeposit.objects.get(id=delete_id)
        deposit.delete()
        messages.success(request, "Transaction Deleted Successfully 👾!")
    return redirect('transactions:deposit')
