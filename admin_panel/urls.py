"""
URL configuration for admin_panel project.
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# View functions untuk halaman-halaman
def dashboard_view(request):
    return render(request, 'admin/dashboard.html')

def penduduk_view(request):
    return render(request, 'admin/penduduk.html')

def surat_view(request):
    return render(request, 'admin/surat.html')

def keuangan_view(request):
    return render(request, 'admin/keuangan.html')

def profil_view(request):
    return render(request, 'admin/profil.html')

def login_view(request):
    return render(request, 'admin/login.html')

def logout_view(request):
    return render(request, 'admin/logout.html')

# Additional views for all admin pages
def analytics_view(request):
    return render(request, 'admin/analytics.html')

def audit_log_view(request):
    return render(request, 'admin/audit_log.html')

def audit_log_lengkap_view(request):
    return render(request, 'admin/audit_log_lengkap.html')

def backup_view(request):
    return render(request, 'admin/backup.html')

def backup_lengkap_view(request):
    return render(request, 'admin/backup_lengkap.html')

def bantuan_view(request):
    return render(request, 'admin/bantuan.html')

def bantuan_lengkap_view(request):
    return render(request, 'admin/bantuan_lengkap.html')

def dashboard_advanced_view(request):
    return render(request, 'admin/dashboard_advanced.html')

def dashboard_main_view(request):
    return render(request, 'admin/dashboard_main.html')

def infrastruktur_view(request):
    return render(request, 'admin/infrastruktur.html')

def infrastruktur_lengkap_view(request):
    return render(request, 'admin/infrastruktur_lengkap.html')

def kegiatan_view(request):
    return render(request, 'admin/kegiatan.html')

def kegiatan_lengkap_view(request):
    return render(request, 'admin/kegiatan_lengkap.html')

def keuangan_lengkap_view(request):
    return render(request, 'admin/keuangan_lengkap.html')

def laporan_view(request):
    return render(request, 'admin/laporan.html')

def laporan_keuangan_view(request):
    return render(request, 'admin/laporan_keuangan.html')

def laporan_keuangan_lengkap_view(request):
    return render(request, 'admin/laporan_keuangan_lengkap.html')

def main_dashboard_view(request):
    return render(request, 'admin/main_dashboard.html')

def monitoring_view(request):
    return render(request, 'admin/monitoring.html')

def monitoring_lengkap_view(request):
    return render(request, 'admin/monitoring_lengkap.html')

def notifikasi_view(request):
    return render(request, 'admin/notifikasi.html')

def notifikasi_lengkap_view(request):
    return render(request, 'admin/notifikasi_lengkap.html')

def penduduk_lengkap_view(request):
    return render(request, 'admin/penduduk_lengkap.html')

def pengaturan_view(request):
    return render(request, 'admin/pengaturan.html')

def surat_lengkap_view(request):
    return render(request, 'admin/surat_lengkap.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Main pages
    path('', dashboard_view, name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('penduduk/', penduduk_view, name='penduduk'),
    path('surat/', surat_view, name='surat'),
    path('keuangan/', keuangan_view, name='keuangan'),
    path('profil/', profil_view, name='profil'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Analytics & Monitoring
    path('admin/analytics/', analytics_view, name='analytics'),
    path('admin/monitoring/', monitoring_view, name='monitoring'),
    path('admin/monitoring-lengkap/', monitoring_lengkap_view, name='monitoring_lengkap'),
    
    # Audit & Security
    path('admin/audit-log/', audit_log_view, name='audit_log'),
    path('admin/audit-log-lengkap/', audit_log_lengkap_view, name='audit_log_lengkap'),
    path('admin/backup/', backup_view, name='backup'),
    path('admin/backup-lengkap/', backup_lengkap_view, name='backup_lengkap'),
    
    # Data Management
    path('admin/kegiatan/', kegiatan_view, name='kegiatan'),
    path('admin/kegiatan-lengkap/', kegiatan_lengkap_view, name='kegiatan_lengkap'),
    path('admin/infrastruktur/', infrastruktur_view, name='infrastruktur'),
    path('admin/infrastruktur-lengkap/', infrastruktur_lengkap_view, name='infrastruktur_lengkap'),
    path('admin/penduduk-lengkap/', penduduk_lengkap_view, name='penduduk_lengkap'),
    path('admin/surat-lengkap/', surat_lengkap_view, name='surat_lengkap'),
    path('admin/keuangan-lengkap/', keuangan_lengkap_view, name='keuangan_lengkap'),
    
    # Reports
    path('admin/laporan/', laporan_view, name='laporan'),
    path('admin/laporan-keuangan/', laporan_keuangan_view, name='laporan_keuangan'),
    path('admin/laporan-keuangan-lengkap/', laporan_keuangan_lengkap_view, name='laporan_keuangan_lengkap'),
    
    # Notifications & Help
    path('admin/notifikasi/', notifikasi_view, name='notifikasi'),
    path('admin/notifikasi-lengkap/', notifikasi_lengkap_view, name='notifikasi_lengkap'),
    path('admin/bantuan/', bantuan_view, name='bantuan'),
    path('admin/bantuan-lengkap/', bantuan_lengkap_view, name='bantuan_lengkap'),
    
    # Settings
    path('admin/pengaturan/', pengaturan_view, name='pengaturan'),
    
    # Dashboard variants
    path('admin/dashboard-advanced/', dashboard_advanced_view, name='dashboard_advanced'),
    path('admin/dashboard-main/', dashboard_main_view, name='dashboard_main'),
    path('admin/main-dashboard/', main_dashboard_view, name='main_dashboard'),
]
