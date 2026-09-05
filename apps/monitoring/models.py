from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel


class SystemMetrics(BaseModel):
    """Model untuk metrics sistem"""
    metric_name = models.CharField(max_length=100)
    metric_value = models.FloatField()
    metric_unit = models.CharField(max_length=20, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_data = models.JSONField(default=dict, blank=True)
    
    class Meta:
        verbose_name = 'System Metrics'
        verbose_name_plural = 'System Metrics'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.metric_name}: {self.metric_value} {self.metric_unit}"


class UserActivity(BaseModel):
    """Model untuk aktivitas user"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    description = models.TextField()
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    session_key = models.CharField(max_length=100, blank=True)
    additional_data = models.JSONField(default=dict, blank=True)
    
    class Meta:
        verbose_name = 'User Activity'
        verbose_name_plural = 'User Activities'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.action}"


class SystemAlert(BaseModel):
    """Model untuk alert sistem"""
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('acknowledged', 'Acknowledged'),
        ('resolved', 'Resolved'),
        ('dismissed', 'Dismissed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    alert_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    acknowledged_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='alerts_acknowledged')
    acknowledged_at = models.DateTimeField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    additional_data = models.JSONField(default=dict, blank=True)
    
    class Meta:
        verbose_name = 'System Alert'
        verbose_name_plural = 'System Alerts'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.severity}"


class BackupLog(BaseModel):
    """Model untuk log backup"""
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    backup_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    file_path = models.CharField(max_length=500, blank=True)
    file_size = models.BigIntegerField(null=True, blank=True)
    started_at = models.DateTimeField()
    completed_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    additional_data = models.JSONField(default=dict, blank=True)
    
    class Meta:
        verbose_name = 'Backup Log'
        verbose_name_plural = 'Backup Logs'
        ordering = ['-started_at']
    
    def __str__(self):
        return f"{self.backup_type} - {self.status}"
    
    @property
    def duration(self):
        if self.completed_at and self.started_at:
            return self.completed_at - self.started_at
        return None


class PerformanceLog(BaseModel):
    """Model untuk log performa"""
    endpoint = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    response_time = models.FloatField()  # dalam milidetik
    status_code = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    additional_data = models.JSONField(default=dict, blank=True)
    
    class Meta:
        verbose_name = 'Performance Log'
        verbose_name_plural = 'Performance Logs'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.method} {self.endpoint} - {self.response_time}ms"
