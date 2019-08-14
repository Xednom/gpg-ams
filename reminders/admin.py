from django.contrib import admin
from jet.filters import DateRangeFilter
from .models import ManagerReminders


class ManagerRemindersProfile(admin.ModelAdmin):
    list_display = ('date', 'due_date', 'requestor', 'requestee', 'comment_from_admin',
                    'memo_from_requestor', 'memo_from_requestee', 'status')
    list_filter = ['date', 'status', 'requestor', 'requestee',
                   ('date', DateRangeFilter)]
    list_per_page = 30
    search_fields = ('manager_under', 'status')
    readonly_fields = ['date']
    fieldsets = (
        ('Reminder Informations', {
            'fields': (
                'date',
                'due_date',
                'requestor',
                'status',
                'comment_from_admin',
                'requestee',
                'memo_from_requestor',
                'memo_from_requestee',
            )
        }),
    )


admin.site.register(ManagerReminders, ManagerRemindersProfile)
