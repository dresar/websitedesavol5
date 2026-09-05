from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel


class KategoriPemasukan(BaseModel):
    """Model untuk kategori pemasukan"""
    nama_kategori = models.CharField(max_length=100)
    kode_kategori = models.CharField(max_length=20, unique=True)
    deskripsi = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Kategori Pemasukan'
        verbose_name_plural = 'Kategori Pemasukan'
        ordering = ['nama_kategori']
    
    def __str__(self):
        return self.nama_kategori


class KategoriPengeluaran(BaseModel):
    """Model untuk kategori pengeluaran"""
    nama_kategori = models.CharField(max_length=100)
    kode_kategori = models.CharField(max_length=20, unique=True)
    deskripsi = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Kategori Pengeluaran'
        verbose_name_plural = 'Kategori Pengeluaran'
        ordering = ['nama_kategori']
    
    def __str__(self):
        return self.nama_kategori


class Pemasukan(BaseModel):
    """Model untuk data pemasukan"""
    kategori = models.ForeignKey(KategoriPemasukan, on_delete=models.CASCADE)
    sumber_pemasukan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=15, decimal_places=2)
    tanggal_pemasukan = models.DateField()
    keterangan = models.TextField(blank=True)
    bukti_transaksi = models.FileField(upload_to='keuangan/pemasukan/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='pemasukan_verified')
    verified_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Pemasukan'
        verbose_name_plural = 'Pemasukan'
        ordering = ['-tanggal_pemasukan']
    
    def __str__(self):
        return f"{self.sumber_pemasukan} - Rp {self.jumlah:,.2f}"


class Pengeluaran(BaseModel):
    """Model untuk data pengeluaran"""
    kategori = models.ForeignKey(KategoriPengeluaran, on_delete=models.CASCADE)
    tujuan_pengeluaran = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=15, decimal_places=2)
    tanggal_pengeluaran = models.DateField()
    keterangan = models.TextField(blank=True)
    bukti_transaksi = models.FileField(upload_to='keuangan/pengeluaran/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='pengeluaran_verified')
    verified_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Pengeluaran'
        verbose_name_plural = 'Pengeluaran'
        ordering = ['-tanggal_pengeluaran']
    
    def __str__(self):
        return f"{self.tujuan_pengeluaran} - Rp {self.jumlah:,.2f}"


class Anggaran(BaseModel):
    """Model untuk anggaran tahunan"""
    TAHUN_CHOICES = [(year, year) for year in range(2020, 2030)]
    
    tahun = models.IntegerField(choices=TAHUN_CHOICES)
    kategori = models.ForeignKey(KategoriPengeluaran, on_delete=models.CASCADE)
    nama_anggaran = models.CharField(max_length=200)
    jumlah_anggaran = models.DecimalField(max_digits=15, decimal_places=2)
    realisasi = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    deskripsi = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Anggaran'
        verbose_name_plural = 'Anggaran'
        unique_together = ['tahun', 'kategori', 'nama_anggaran']
        ordering = ['-tahun', 'kategori']
    
    def __str__(self):
        return f"{self.tahun} - {self.nama_anggaran}"
    
    @property
    def sisa_anggaran(self):
        return self.jumlah_anggaran - self.realisasi
    
    @property
    def persentase_realisasi(self):
        if self.jumlah_anggaran > 0:
            return (self.realisasi / self.jumlah_anggaran) * 100
        return 0


class SaldoKas(BaseModel):
    """Model untuk saldo kas"""
    tanggal = models.DateField(unique=True)
    saldo_awal = models.DecimalField(max_digits=15, decimal_places=2)
    total_pemasukan = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_pengeluaran = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    saldo_akhir = models.DecimalField(max_digits=15, decimal_places=2)
    keterangan = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Saldo Kas'
        verbose_name_plural = 'Saldo Kas'
        ordering = ['-tanggal']
    
    def __str__(self):
        return f"{self.tanggal} - Rp {self.saldo_akhir:,.2f}"
    
    def save(self, *args, **kwargs):
        self.saldo_akhir = self.saldo_awal + self.total_pemasukan - self.total_pengeluaran
        super().save(*args, **kwargs)
