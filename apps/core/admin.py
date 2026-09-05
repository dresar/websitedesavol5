from django.contrib import admin
from django.utils.html import format_html
from .models import Desa, AuditLog, SystemSettings


@admin.register(Desa)
class DesaAdmin(admin.ModelAdmin):
    list_display = ['nama_desa', 'kode_desa', 'kecamatan', 'kabupaten', 'kepala_desa', 'is_active']
    list_filter = ['is_active', 'kecamatan', 'kabupaten', 'provinsi']
    search_fields = ['nama_desa', 'kode_desa', 'kepala_desa']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Data Desa', {
            'fields': ('nama_desa', 'kode_desa', 'alamat', 'kode_pos')
        }),
        ('Wilayah', {
            'fields': ('kecamatan', 'kabupaten', 'provinsi')
        }),
        ('Pemerintahan', {
            'fields': ('kepala_desa', 'sekretaris_desa', 'bendahara_desa')
        }),
        ('Media', {
            'fields': ('logo',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'model_name', 'object_id', 'ip_address', 'created_at']
    list_filter = ['action', 'model_name', 'created_at']
    search_fields = ['user__username', 'model_name', 'object_id', 'description']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(SystemSettings)
class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'data_type', 'description']
    list_filter = ['data_type']
    search_fields = ['key', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('key')
