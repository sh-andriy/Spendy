import requests
from .models import Balance


def nav(request):
    if request.user.is_authenticated:
        response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5').json()
        usd_price = float(response[0]['buy'])
        user_balance = Balance.objects.get(user=request.user)
        return {
            'usd_price': usd_price,
            'user_balance': user_balance,
        }
    return {}

