from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModel(models.Model):
    """Base model dengan field umum untuk semua model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_updated')
    
    class Meta:
        abstract = True


class Desa(BaseModel):
    """Model untuk data desa"""
    nama_desa = models.CharField(max_length=100)
    kode_desa = models.CharField(max_length=10, unique=True)
    alamat = models.TextField()
    kode_pos = models.CharField(max_length=10)
    kecamatan = models.CharField(max_length=100)
    kabupaten = models.CharField(max_length=100)
    provinsi = models.CharField(max_length=100)
    kepala_desa = models.CharField(max_length=100)
    sekretaris_desa = models.CharField(max_length=100)
    bendahara_desa = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='desa/logo/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Desa'
        verbose_name_plural = 'Data Desa'
    
    def __str__(self):
        return self.nama_desa


class AuditLog(BaseModel):
    """Model untuk audit log"""
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
        ('VIEW', 'View'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    
    class Meta:
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.model_name}"


class SystemSettings(BaseModel):
    """Model untuk pengaturan sistem"""
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True)
    data_type = models.CharField(max_length=20, choices=[
        ('string', 'String'),
        ('integer', 'Integer'),
        ('boolean', 'Boolean'),
        ('json', 'JSON'),
    ], default='string')
    
    class Meta:
        verbose_name = 'System Setting'
        verbose_name_plural = 'System Settings'
    
    def __str__(self):
        return self.key
