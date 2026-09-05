from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel


class Penduduk(BaseModel):
    """Model untuk data penduduk"""
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    
    STATUS_KAWIN_CHOICES = [
        ('belum_kawin', 'Belum Kawin'),
        ('kawin', 'Kawin'),
        ('cerai_hidup', 'Cerai Hidup'),
        ('cerai_mati', 'Cerai Mati'),
    ]
    
    AGAMA_CHOICES = [
        ('islam', 'Islam'),
        ('kristen', 'Kristen'),
        ('katolik', 'Katolik'),
        ('hindu', 'Hindu'),
        ('buddha', 'Buddha'),
        ('khonghucu', 'Khonghucu'),
    ]
    
    PENDIDIKAN_CHOICES = [
        ('tidak_sekolah', 'Tidak Sekolah'),
        ('tidak_tamat_sd', 'Tidak Tamat SD'),
        ('tamat_sd', 'Tamat SD'),
        ('tamat_smp', 'Tamat SMP'),
        ('tamat_sma', 'Tamat SMA'),
        ('tamat_diploma', 'Tamat Diploma'),
        ('tamat_sarjana', 'Tamat Sarjana'),
        ('tamat_pascasarjana', 'Tamat Pascasarjana'),
    ]
    
    PEKERJAAN_CHOICES = [
        ('tidak_bekerja', 'Tidak Bekerja'),
        ('pelajar', 'Pelajar'),
        ('mahasiswa', 'Mahasiswa'),
        ('pns', 'PNS'),
        ('tni', 'TNI'),
        ('polri', 'Polri'),
        ('karyawan_swasta', 'Karyawan Swasta'),
        ('wiraswasta', 'Wiraswasta'),
        ('petani', 'Petani'),
        ('nelayan', 'Nelayan'),
        ('buruh', 'Buruh'),
        ('pensiunan', 'Pensiunan'),
        ('lainnya', 'Lainnya'),
    ]
    
    # Data Pribadi
    nik = models.CharField(max_length=16, unique=True, verbose_name='NIK')
    nama_lengkap = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    agama = models.CharField(max_length=20, choices=AGAMA_CHOICES)
    status_kawin = models.CharField(max_length=20, choices=STATUS_KAWIN_CHOICES)
    pendidikan = models.CharField(max_length=30, choices=PENDIDIKAN_CHOICES)
    pekerjaan = models.CharField(max_length=30, choices=PEKERJAAN_CHOICES)
    
    # Data Alamat
    alamat = models.TextField()
    rt = models.CharField(max_length=3)
    rw = models.CharField(max_length=3)
    dusun = models.CharField(max_length=100)
    
    # Data Keluarga
    nama_ayah = models.CharField(max_length=100, blank=True)
    nama_ibu = models.CharField(max_length=100, blank=True)
    nama_pasangan = models.CharField(max_length=100, blank=True)
    
    # Data Kontak
    no_telepon = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    
    # Data Tambahan
    foto = models.ImageField(upload_to='penduduk/foto/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    keterangan = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Penduduk'
        verbose_name_plural = 'Data Penduduk'
        ordering = ['nama_lengkap']
    
    def __str__(self):
        return f"{self.nama_lengkap} - {self.nik}"
    
    @property
    def umur(self):
        from datetime import date
        today = date.today()
        return today.year - self.tanggal_lahir.year - ((today.month, today.day) < (self.tanggal_lahir.month, self.tanggal_lahir.day))


class Keluarga(BaseModel):
    """Model untuk data keluarga"""
    nomor_kk = models.CharField(max_length=16, unique=True, verbose_name='Nomor KK')
    kepala_keluarga = models.ForeignKey(Penduduk, on_delete=models.CASCADE, related_name='kepala_keluarga')
    alamat = models.TextField()
    rt = models.CharField(max_length=3)
    rw = models.CharField(max_length=3)
    dusun = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Keluarga'
        verbose_name_plural = 'Data Keluarga'
        ordering = ['nomor_kk']
    
    def __str__(self):
        return f"{self.nomor_kk} - {self.kepala_keluarga.nama_lengkap}"


class AnggotaKeluarga(BaseModel):
    """Model untuk anggota keluarga"""
    keluarga = models.ForeignKey(Keluarga, on_delete=models.CASCADE, related_name='anggota')
    penduduk = models.ForeignKey(Penduduk, on_delete=models.CASCADE)
    status_hubungan = models.CharField(max_length=30, choices=[
        ('kepala_keluarga', 'Kepala Keluarga'),
        ('istri', 'Istri'),
        ('anak', 'Anak'),
        ('menantu', 'Menantu'),
        ('cucu', 'Cucu'),
        ('orang_tua', 'Orang Tua'),
        ('mertua', 'Mertua'),
        ('famili_lain', 'Famili Lain'),
        ('pembantu', 'Pembantu'),
        ('lainnya', 'Lainnya'),
    ])
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Anggota Keluarga'
        verbose_name_plural = 'Anggota Keluarga'
        unique_together = ['keluarga', 'penduduk']
    
    def __str__(self):
        return f"{self.keluarga.nomor_kk} - {self.penduduk.nama_lengkap}"
