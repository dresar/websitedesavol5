from django.contrib import admin
from .models import JenisLaporan, Laporan, TemplateLaporan, ExportLaporan


@admin.register(JenisLaporan)
class JenisLaporanAdmin(admin.ModelAdmin):
    list_display = ['nama_laporan', 'kode_laporan', 'is_active']
    list_filter = ['is_active']
    search_fields = ['nama_laporan', 'kode_laporan']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Laporan', {
            'fields': ('nama_laporan', 'kode_laporan', 'deskripsi')
        }),
        ('Template', {
            'fields': ('template_laporan',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Laporan)
class LaporanAdmin(admin.ModelAdmin):
    list_display = ['judul_laporan', 'jenis_laporan', 'periode_awal', 'periode_akhir', 'status', 'approved_by']
    list_filter = ['status', 'jenis_laporan', 'periode_awal', 'approved_by']
    search_fields = ['judul_laporan', 'konten_laporan']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'periode_awal'
    
    fieldsets = (
        ('Data Laporan', {
            'fields': ('jenis_laporan', 'judul_laporan', 'periode_awal', 'periode_akhir')
        }),
        ('Status & Persetujuan', {
            'fields': ('status', 'approved_by', 'approved_at', 'rejected_reason')
        }),
        ('Konten & File', {
            'fields': ('konten_laporan', 'file_laporan')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TemplateLaporan)
class TemplateLaporanAdmin(admin.ModelAdmin):
    list_display = ['jenis_laporan', 'nama_template', 'is_default']
    list_filter = ['is_default', 'jenis_laporan']
    search_fields = ['nama_template', 'jenis_laporan__nama_laporan']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Template', {
            'fields': ('jenis_laporan', 'nama_template', 'is_default')
        }),
        ('Konten', {
            'fields': ('konten_template', 'variabel_template')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ExportLaporan)
class ExportLaporanAdmin(admin.ModelAdmin):
    list_display = ['laporan', 'format_file', 'status', 'created_at']
    list_filter = ['format_file', 'status', 'created_at']
    search_fields = ['laporan__judul_laporan']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Export', {
            'fields': ('laporan', 'format_file', 'file_export')
        }),
        ('Status', {
            'fields': ('status', 'error_message')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
