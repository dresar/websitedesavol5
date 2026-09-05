from django.contrib import admin
from .models import SystemMetrics, UserActivity, SystemAlert, BackupLog, PerformanceLog


@admin.register(SystemMetrics)
class SystemMetricsAdmin(admin.ModelAdmin):
    list_display = ['metric_name', 'metric_value', 'metric_unit', 'timestamp']
    list_filter = ['metric_name', 'timestamp']
    search_fields = ['metric_name']
    readonly_fields = ['created_at', 'updated_at', 'timestamp']
    date_hierarchy = 'timestamp'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'ip_address', 'created_at']
    list_filter = ['action', 'created_at']
    search_fields = ['user__username', 'action', 'description']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(SystemAlert)
class SystemAlertAdmin(admin.ModelAdmin):
    list_display = ['title', 'severity', 'status', 'is_active', 'created_at']
    list_filter = ['severity', 'status', 'is_active', 'alert_type', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Data Alert', {
            'fields': ('title', 'description', 'alert_type')
        }),
        ('Severity & Status', {
            'fields': ('severity', 'status', 'is_active')
        }),
        ('Acknowledgment', {
            'fields': ('acknowledged_by', 'acknowledged_at', 'resolved_at')
        }),
        ('Additional Data', {
            'fields': ('additional_data',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(BackupLog)
class BackupLogAdmin(admin.ModelAdmin):
    list_display = ['backup_type', 'status', 'file_size', 'started_at', 'completed_at', 'duration']
    list_filter = ['backup_type', 'status', 'started_at']
    search_fields = ['backup_type', 'error_message']
    readonly_fields = ['created_at', 'updated_at', 'duration']
    date_hierarchy = 'started_at'
    
    fieldsets = (
        ('Data Backup', {
            'fields': ('backup_type', 'status', 'file_path', 'file_size')
        }),
        ('Waktu', {
            'fields': ('started_at', 'completed_at', 'duration')
        }),
        ('Error & Data', {
            'fields': ('error_message', 'additional_data')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PerformanceLog)
class PerformanceLogAdmin(admin.ModelAdmin):
    list_display = ['endpoint', 'method', 'response_time', 'status_code', 'user', 'created_at']
    list_filter = ['method', 'status_code', 'created_at']
    search_fields = ['endpoint', 'user__username']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
