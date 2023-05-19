from django.contrib import admin
from .models import Transaction, Balance, Category, CreditDeposit

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ("name", "id")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "amount")
    search_fields = ("id", "user", "amount")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'category')
    search_fields = ('id', 'balance', 'category')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(CreditDeposit)
class CreditDepositAdmin(admin.ModelAdmin):
    list_display = ("id", 'balance', 'amount')
    search_fields = ("id", 'balance', 'amount')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
