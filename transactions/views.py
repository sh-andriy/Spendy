from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError


def add_income(request):
    return render(request, 'transactions/add_income.html')


def add_expense(request):
    return render(request, 'transactions/add_expense.html')
