from django.contrib import admin
from .models import chaiVariety, ChaiReview, Store, chaicertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class chaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'date_added')
    search_fields = ('name', 'chai_type')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('chais_available',)

class chaicertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issue_date', 'expiry_date')
    search_fields = ('chai__name', 'certificate_number')

admin.site.register(chaiVariety, chaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(chaicertificate, chaicertificateAdmin)