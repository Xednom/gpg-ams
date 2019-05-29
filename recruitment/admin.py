from django.contrib import admin

from .models import Resume, Reference


class ReferenceInline(admin.TabularInline):
    model = Reference
    extra = 1


class ResumeProfile(admin.ModelAdmin):
    inlines = [ReferenceInline]
    list_display = ('name', 'phone_number', 'email', 
                    'educational_attainment', 'date_created')
    list_filter = ('name',)
    search_fields = ('name', 'reference_contact', 'email')
    readonly_fields = ['date_created']
    fieldsets = (
        ("Personal Informations", {
            'fields': (
                'name',
                'date_of_birth',
                'phone_number',
                'email',
                'educational_attainment',
                'work_experience',
                'attachment',
            )
        }),
        ("Other informations", {
            'fields': (
                'training_workshop_seminar_attended',
                'reference_contact',
                'communication_assessment',
                'other_skills',
                'notes',
            )
        }),
        ("Important Information", {
            'fields': (
                'date_created',
            )
        }),
    )


admin.site.register(Resume, ResumeProfile)
