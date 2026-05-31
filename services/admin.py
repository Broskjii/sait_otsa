from django.contrib import admin
from .models import ServiceRequest, ContactInfo


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'phone', 'created_at', 'is_processed')
    list_filter = ('service_type', 'is_processed', 'created_at')
    search_fields = ('name', 'phone', 'email', 'message')
    list_editable = ('is_processed',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Информация о заявке', {
            'fields': ('service_type', 'name', 'phone', 'email')
        }),
        ('Детали', {
            'fields': ('message', 'created_at')
        }),
        ('Статус', {
            'fields': ('is_processed',)
        }),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'work_hours')
    
    def has_add_permission(self, request):
        # Разрешаем создать только одну запись с контактами
        return not ContactInfo.objects.exists()