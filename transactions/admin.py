from django.contrib import admin
from .models import Transaction, Balance, Category, CreditDeposit

# Register your models here.


admin.site.register(Balance)
admin.site.register(CreditDeposit)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ("name", "id")

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
