from django.contrib import admin
from django.utils.html import format_html
from .models import JenisSurat, Surat, TemplateSurat, PersyaratanSurat, DokumenSurat


@admin.register(JenisSurat)
class JenisSuratAdmin(admin.ModelAdmin):
    list_display = ['nama_surat', 'kode_surat', 'biaya', 'is_active']
    list_filter = ['is_active']
    search_fields = ['nama_surat', 'kode_surat']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Surat', {
            'fields': ('nama_surat', 'kode_surat', 'biaya')
        }),
        ('Template', {
            'fields': ('template_surat',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Surat)
class SuratAdmin(admin.ModelAdmin):
    list_display = ['nomor_surat', 'jenis_surat', 'penduduk', 'status', 'tanggal_surat', 'approved_by']
    list_filter = ['status', 'jenis_surat', 'tanggal_surat', 'approved_by']
    search_fields = ['nomor_surat', 'penduduk__nama_lengkap', 'penduduk__nik']
    readonly_fields = ['created_at', 'updated_at', 'nomor_surat']
    date_hierarchy = 'tanggal_surat'
    
    fieldsets = (
        ('Data Surat', {
            'fields': ('jenis_surat', 'penduduk', 'nomor_surat', 'tanggal_surat')
        }),
        ('Status & Persetujuan', {
            'fields': ('status', 'approved_by', 'approved_at', 'rejected_reason')
        }),
        ('Keterangan & File', {
            'fields': ('keterangan', 'file_surat')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TemplateSurat)
class TemplateSuratAdmin(admin.ModelAdmin):
    list_display = ['jenis_surat', 'nama_template', 'is_default']
    list_filter = ['is_default', 'jenis_surat']
    search_fields = ['nama_template', 'jenis_surat__nama_surat']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Template', {
            'fields': ('jenis_surat', 'nama_template', 'is_default')
        }),
        ('Konten', {
            'fields': ('konten_template', 'variabel_template')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PersyaratanSurat)
class PersyaratanSuratAdmin(admin.ModelAdmin):
    list_display = ['jenis_surat', 'nama_persyaratan', 'is_wajib', 'urutan']
    list_filter = ['is_wajib', 'jenis_surat']
    search_fields = ['nama_persyaratan', 'jenis_surat__nama_surat']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['jenis_surat', 'urutan']
    
    fieldsets = (
        ('Data Persyaratan', {
            'fields': ('jenis_surat', 'nama_persyaratan', 'deskripsi')
        }),
        ('Pengaturan', {
            'fields': ('is_wajib', 'urutan')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(DokumenSurat)
class DokumenSuratAdmin(admin.ModelAdmin):
    list_display = ['surat', 'nama_dokumen', 'file_dokumen']
    list_filter = ['surat__jenis_surat']
    search_fields = ['nama_dokumen', 'surat__nomor_surat']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Dokumen', {
            'fields': ('surat', 'nama_dokumen', 'file_dokumen')
        }),
        ('Deskripsi', {
            'fields': ('deskripsi',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
