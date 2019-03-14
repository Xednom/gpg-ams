from django.contrib import admin

from .models import (
    DueDiligence,
    LandData,
    AdditionalLandInfo,
    CountyData,
    TaxData,
    ZoningData,
    DataOnUtilities
    )


class LandDataDetail(admin.StackedInline):
    model = LandData

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1
        return max_num


class AdditionalLandInfoDetail(admin.StackedInline):
    model = AdditionalLandInfo
    
    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1
        return max_num


class CountyDataDetail(admin.StackedInline):
    model = CountyData

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1
        return max_num


class TaxDataDetail(admin.StackedInline):
    model = TaxData

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1
        return max_num


class ZoningDataDetail(admin.StackedInline):
    model = ZoningData

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1
        return max_num


class DataOnUtilitiesDetail(admin.StackedInline):
    model = DataOnUtilities

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1
        return max_num


class DueDiligenceProfile(admin.ModelAdmin):
    inlines = (LandDataDetail, AdditionalLandInfoDetail,
               CountyDataDetail, TaxDataDetail,
               ZoningDataDetail, DataOnUtilitiesDetail)
    list_display = ('date_requested', 'company_name', 'company_owner', 'date_completed_or_returned')
    search_fields = ('company_name__name', 'company_owner')
    fieldsets = (
        ('Due Diligence client Information', {
            'fields': (
                'date_requested',
                'company_name',
                'company_owner',
                'date_completed_or_returned',
            )
        }),
    )


admin.site.register(DueDiligence, DueDiligenceProfile)
