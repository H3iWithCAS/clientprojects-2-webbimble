from django.contrib import admin
from .models import Child

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'parent_name', 'contact_number', 'enrollment_date')
    list_filter = ('gender', 'enrollment_date')
    search_fields = ('name', 'parent_name')
    ordering = ('-enrollment_date',)