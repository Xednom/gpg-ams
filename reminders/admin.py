from django.contrib import admin

from .models import ManagerReminders


class ManagerRemindersProfile(admin.ModelAdmin):
    list_display = ('date', 'due_date', 'manager_under', 'status')
    search_fields = ('manager_under', 'status')
    readonly_fields = ['date']
    fieldsets = (
        ('Reminder Informations', {
            'fields': (
                'date',
                'due_date',
                'manager_under',
                'status',
                'description',
                'notes_from_company',
                'notes_from_manager',
            )
        }),
    )


admin.site.register(ManagerReminders, ManagerRemindersProfile)