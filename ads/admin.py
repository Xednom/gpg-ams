from django.contrib import admin

from jet.filters import DateRangeFilter
from .models import AdsContent


class AdsContentProfile(admin.ModelAdmin):
    list_display = ('date_requested', 'due_date', 'date_completed', 'client',
                    'apn_or_items_needs_ad_content', 'final_title', 'content_status',
                    'ads_writer')
    list_filter = ('date_requested', 'due_date',
                   'date_completed', 'client', 'content_status',
                   ('date_requested', DateRangeFilter),
                   ('due_date', DateRangeFilter),
                   ('date_completed', DateRangeFilter))
    search_fields = ('client__full_name', 'ads_writer__full_name',
                     'final_title')
    readonly_fields = ('date_requested',)
    fieldsets = (
        ('Ads Content Information', {
            'fields': (
                'date_requested',
                'due_date',
                'date_completed',
                'client',
                'ads_writer',
                'apn_or_items_needs_ad_content',
                'client_recommendation',
                'content_instruction',
                'content_finished',
                'final_title',
                'modification',
                'content_status',
                'additional_notes',
            )
        }),
    )


admin.site.register(AdsContent, AdsContentProfile)
