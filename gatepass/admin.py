from django.contrib import admin
from .models import GatePass

@admin.register(GatePass)
class GatePassAdmin(admin.ModelAdmin):
    list_display = ('gate_pass_number', 'visitor_name', 'organization', 'date_of_entry', 'time_of_entry', 'status')
    search_fields = ('visitor_name', 'organization', 'gate_pass_number')
    list_filter = ('status', 'date_of_entry')
    ordering = ('-date_of_entry',)