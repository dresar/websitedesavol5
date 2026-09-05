from django.contrib import admin
from django.utils.html import format_html
from .models import Penduduk, Keluarga, AnggotaKeluarga


@admin.register(Penduduk)
class PendudukAdmin(admin.ModelAdmin):
    list_display = ['nik', 'nama_lengkap', 'jenis_kelamin', 'umur', 'alamat', 'is_active']
    list_filter = ['jenis_kelamin', 'agama', 'status_kawin', 'pendidikan', 'pekerjaan', 'is_active']
    search_fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    readonly_fields = ['created_at', 'updated_at', 'umur']
    date_hierarchy = 'tanggal_lahir'
    
    fieldsets = (
        ('Data Pribadi', {
            'fields': ('nik', 'nama_lengkap', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'agama')
        }),
        ('Status & Pendidikan', {
            'fields': ('status_kawin', 'pendidikan', 'pekerjaan')
        }),
        ('Alamat', {
            'fields': ('alamat', 'rt', 'rw', 'dusun')
        }),
        ('Data Keluarga', {
            'fields': ('nama_ayah', 'nama_ibu', 'nama_pasangan')
        }),
        ('Kontak', {
            'fields': ('no_telepon', 'email')
        }),
        ('Media & Status', {
            'fields': ('foto', 'is_active', 'keterangan')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Keluarga)
class KeluargaAdmin(admin.ModelAdmin):
    list_display = ['nomor_kk', 'kepala_keluarga', 'alamat', 'rt', 'rw', 'is_active']
    list_filter = ['is_active', 'rt', 'rw', 'dusun']
    search_fields = ['nomor_kk', 'kepala_keluarga__nama_lengkap', 'alamat']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data KK', {
            'fields': ('nomor_kk', 'kepala_keluarga')
        }),
        ('Alamat', {
            'fields': ('alamat', 'rt', 'rw', 'dusun')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AnggotaKeluarga)
class AnggotaKeluargaAdmin(admin.ModelAdmin):
    list_display = ['keluarga', 'penduduk', 'status_hubungan', 'is_active']
    list_filter = ['status_hubungan', 'is_active']
    search_fields = ['keluarga__nomor_kk', 'penduduk__nama_lengkap']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Anggota', {
            'fields': ('keluarga', 'penduduk', 'status_hubungan')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
