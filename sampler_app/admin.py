from django.contrib import admin
from .models import Sample, HazardType

class SampleAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_id', 'sample_name', 'subject', 'submission_date', 'expiration_date', 'unique_code')
    list_filter = ('user_type', 'hazard', 'submission_date', 'expiration_date')  # Add filters as needed
    search_fields = ('user_name', 'user_id', 'sample_name', 'subject')  # Add search fields as needed
    readonly_fields = ('submission_date', 'unique_code')

    fieldsets = (
        ('User Information', {
            'fields': ('user_type', 'user_name', 'user_id'),
        }),
        ('Sample Information', {
            'fields': ('sample_name', 'subject', 'hazard', 'expiration_date'),
        }),
        ('Auto-Generated Fields', {
            'fields': ('submission_date', 'unique_code'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Sample, SampleAdmin)
admin.site.register(HazardType)
