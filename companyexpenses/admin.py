from django.contrib import admin
from jet.filters import DateRangeFilter
from .models import Expenses, Type

class ExpensesProfile(admin.ModelAdmin):
    list_display = ('month', 'date', 'next_due_date',
                    'type', 'amount', 'payment_channel')
    list_filter = ['month', 'date', 'type', 'payment_channel',
                   'category', 'tagging', 'status',
                   ('date', DateRangeFilter)]
    list_per_page = 30
    search_fields = ('category', 'referrence', 'payment_channel')
    fieldsets = (
        ("Company Expenses Informations", {
            'fields': (
                'month',
                'date',
                'description',
                'amount',
                'type',
                'category',
                'tagging',
                'next_due_date',
                'status',
                'payment_channel',
                'referrence',
                'notes'
            )
        }),
    )


admin.site.register(Expenses, ExpensesProfile)
admin.site.register(Type)
