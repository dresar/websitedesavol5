from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel
from apps.penduduk.models import Penduduk


class JenisSurat(BaseModel):
    """Model untuk jenis-jenis surat"""
    nama_surat = models.CharField(max_length=100)
    kode_surat = models.CharField(max_length=20, unique=True)
    template_surat = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    biaya = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        verbose_name = 'Jenis Surat'
        verbose_name_plural = 'Jenis Surat'
        ordering = ['nama_surat']
    
    def __str__(self):
        return self.nama_surat


class Surat(BaseModel):
    """Model untuk surat menyurat"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Menunggu Persetujuan'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
        ('completed', 'Selesai'),
    ]
    
    jenis_surat = models.ForeignKey(JenisSurat, on_delete=models.CASCADE)
    penduduk = models.ForeignKey(Penduduk, on_delete=models.CASCADE)
    nomor_surat = models.CharField(max_length=50, unique=True)
    tanggal_surat = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    keterangan = models.TextField(blank=True)
    file_surat = models.FileField(upload_to='surat/files/', null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='surat_approved')
    approved_at = models.DateTimeField(null=True, blank=True)
    rejected_reason = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Surat'
        verbose_name_plural = 'Surat'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.nomor_surat} - {self.penduduk.nama_lengkap}"
    
    def save(self, *args, **kwargs):
        if not self.nomor_surat:
            # Generate nomor surat otomatis
            from datetime import datetime
            year = datetime.now().year
            count = Surat.objects.filter(jenis_surat=self.jenis_surat, tanggal_surat__year=year).count() + 1
            self.nomor_surat = f"{self.jenis_surat.kode_surat}/{count:03d}/{year}"
        super().save(*args, **kwargs)


class TemplateSurat(BaseModel):
    """Model untuk template surat"""
    jenis_surat = models.ForeignKey(JenisSurat, on_delete=models.CASCADE)
    nama_template = models.CharField(max_length=100)
    konten_template = models.TextField()
    variabel_template = models.JSONField(default=list, help_text="Daftar variabel yang bisa digunakan dalam template")
    is_default = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Template Surat'
        verbose_name_plural = 'Template Surat'
    
    def __str__(self):
        return f"{self.jenis_surat.nama_surat} - {self.nama_template}"


class PersyaratanSurat(BaseModel):
    """Model untuk persyaratan surat"""
    jenis_surat = models.ForeignKey(JenisSurat, on_delete=models.CASCADE)
    nama_persyaratan = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    is_wajib = models.BooleanField(default=True)
    urutan = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = 'Persyaratan Surat'
        verbose_name_plural = 'Persyaratan Surat'
        ordering = ['urutan', 'nama_persyaratan']
    
    def __str__(self):
        return f"{self.jenis_surat.nama_surat} - {self.nama_persyaratan}"


class DokumenSurat(BaseModel):
    """Model untuk dokumen pendukung surat"""
    surat = models.ForeignKey(Surat, on_delete=models.CASCADE, related_name='dokumen')
    nama_dokumen = models.CharField(max_length=200)
    file_dokumen = models.FileField(upload_to='surat/dokumen/')
    deskripsi = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Dokumen Surat'
        verbose_name_plural = 'Dokumen Surat'
    
    def __str__(self):
        return f"{self.surat.nomor_surat} - {self.nama_dokumen}"
