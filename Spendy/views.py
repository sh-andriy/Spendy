from django.shortcuts import redirect


def index(request):
    return redirect('transactions:home')
