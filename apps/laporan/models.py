from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel


class JenisLaporan(BaseModel):
    """Model untuk jenis laporan"""
    nama_laporan = models.CharField(max_length=100)
    kode_laporan = models.CharField(max_length=20, unique=True)
    deskripsi = models.TextField(blank=True)
    template_laporan = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Jenis Laporan'
        verbose_name_plural = 'Jenis Laporan'
        ordering = ['nama_laporan']
    
    def __str__(self):
        return self.nama_laporan


class Laporan(BaseModel):
    """Model untuk laporan"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Menunggu Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
        ('published', 'Dipublikasikan'),
    ]
    
    jenis_laporan = models.ForeignKey(JenisLaporan, on_delete=models.CASCADE)
    judul_laporan = models.CharField(max_length=200)
    periode_awal = models.DateField()
    periode_akhir = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    konten_laporan = models.TextField()
    file_laporan = models.FileField(upload_to='laporan/files/', null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='laporan_approved')
    approved_at = models.DateTimeField(null=True, blank=True)
    rejected_reason = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Laporan'
        verbose_name_plural = 'Laporan'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.judul_laporan} - {self.periode_awal} s/d {self.periode_akhir}"


class TemplateLaporan(BaseModel):
    """Model untuk template laporan"""
    jenis_laporan = models.ForeignKey(JenisLaporan, on_delete=models.CASCADE)
    nama_template = models.CharField(max_length=100)
    konten_template = models.TextField()
    variabel_template = models.JSONField(default=list, help_text="Daftar variabel yang bisa digunakan dalam template")
    is_default = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Template Laporan'
        verbose_name_plural = 'Template Laporan'
    
    def __str__(self):
        return f"{self.jenis_laporan.nama_laporan} - {self.nama_template}"


class ExportLaporan(BaseModel):
    """Model untuk export laporan"""
    FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('excel', 'Excel'),
        ('csv', 'CSV'),
        ('word', 'Word'),
    ]
    
    laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    format_file = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    file_export = models.FileField(upload_to='laporan/export/')
    status = models.CharField(max_length=20, choices=[
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='processing')
    error_message = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Export Laporan'
        verbose_name_plural = 'Export Laporan'
    
    def __str__(self):
        return f"{self.laporan.judul_laporan} - {self.format_file.upper()}"
