from django.contrib import admin
from .models import firstVariety, firstVarietyCertificate, Store, firstVarietyReview

class firstReviewInline(admin.TabularInline):
    model = firstVarietyReview
    extra = 0

class firstVarietyAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_added', 'type']
    inlines = [firstReviewInline]
    
class storeadmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    filter_horizontal = ['first_varieties']

class certificateadmin(admin.ModelAdmin):
    list_display = ['first', 'certifcate_number', 'date_issued', 'date_expired']

admin.site.register(firstVariety, firstVarietyAdmin)
admin.site.register(Store, storeadmin)
admin.site.register(firstVarietyCertificate, certificateadmin)