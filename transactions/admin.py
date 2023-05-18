from django.contrib import admin
from .models import Transaction, Balance, Category, CreditDeposit

# Register your models here.


admin.site.register(Balance)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(CreditDeposit)
