from django.contrib import admin
from django.utils.html import format_html
from .models import (
    KategoriPemasukan, KategoriPengeluaran, Pemasukan, Pengeluaran, 
    Anggaran, SaldoKas
)


@admin.register(KategoriPemasukan)
class KategoriPemasukanAdmin(admin.ModelAdmin):
    list_display = ['nama_kategori', 'kode_kategori', 'is_active']
    list_filter = ['is_active']
    search_fields = ['nama_kategori', 'kode_kategori']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Kategori', {
            'fields': ('nama_kategori', 'kode_kategori', 'deskripsi')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(KategoriPengeluaran)
class KategoriPengeluaranAdmin(admin.ModelAdmin):
    list_display = ['nama_kategori', 'kode_kategori', 'is_active']
    list_filter = ['is_active']
    search_fields = ['nama_kategori', 'kode_kategori']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Data Kategori', {
            'fields': ('nama_kategori', 'kode_kategori', 'deskripsi')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Pemasukan)
class PemasukanAdmin(admin.ModelAdmin):
    list_display = ['sumber_pemasukan', 'kategori', 'jumlah', 'tanggal_pemasukan', 'is_verified']
    list_filter = ['kategori', 'tanggal_pemasukan', 'is_verified']
    search_fields = ['sumber_pemasukan', 'keterangan']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'tanggal_pemasukan'
    
    fieldsets = (
        ('Data Pemasukan', {
            'fields': ('kategori', 'sumber_pemasukan', 'jumlah', 'tanggal_pemasukan')
        }),
        ('Verifikasi', {
            'fields': ('is_verified', 'verified_by', 'verified_at')
        }),
        ('Keterangan & File', {
            'fields': ('keterangan', 'bukti_transaksi')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Pengeluaran)
class PengeluaranAdmin(admin.ModelAdmin):
    list_display = ['tujuan_pengeluaran', 'kategori', 'jumlah', 'tanggal_pengeluaran', 'is_verified']
    list_filter = ['kategori', 'tanggal_pengeluaran', 'is_verified']
    search_fields = ['tujuan_pengeluaran', 'keterangan']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'tanggal_pengeluaran'
    
    fieldsets = (
        ('Data Pengeluaran', {
            'fields': ('kategori', 'tujuan_pengeluaran', 'jumlah', 'tanggal_pengeluaran')
        }),
        ('Verifikasi', {
            'fields': ('is_verified', 'verified_by', 'verified_at')
        }),
        ('Keterangan & File', {
            'fields': ('keterangan', 'bukti_transaksi')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Anggaran)
class AnggaranAdmin(admin.ModelAdmin):
    list_display = ['tahun', 'nama_anggaran', 'kategori', 'jumlah_anggaran', 'realisasi', 'sisa_anggaran', 'persentase_realisasi']
    list_filter = ['tahun', 'kategori', 'is_active']
    search_fields = ['nama_anggaran', 'deskripsi']
    readonly_fields = ['created_at', 'updated_at', 'sisa_anggaran', 'persentase_realisasi']
    
    fieldsets = (
        ('Data Anggaran', {
            'fields': ('tahun', 'kategori', 'nama_anggaran', 'jumlah_anggaran')
        }),
        ('Realisasi', {
            'fields': ('realisasi', 'sisa_anggaran', 'persentase_realisasi')
        }),
        ('Deskripsi & Status', {
            'fields': ('deskripsi', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SaldoKas)
class SaldoKasAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'saldo_awal', 'total_pemasukan', 'total_pengeluaran', 'saldo_akhir']
    list_filter = ['tanggal']
    search_fields = ['keterangan']
    readonly_fields = ['created_at', 'updated_at', 'saldo_akhir']
    date_hierarchy = 'tanggal'
    
    fieldsets = (
        ('Data Saldo', {
            'fields': ('tanggal', 'saldo_awal', 'total_pemasukan', 'total_pengeluaran', 'saldo_akhir')
        }),
        ('Keterangan', {
            'fields': ('keterangan',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
