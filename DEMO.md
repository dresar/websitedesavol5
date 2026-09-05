# Demo Panel Admin Desa

## 🚀 Cara Menjalankan Proyek

### Opsi 1: Menggunakan Setup Script (Recommended)

**Windows:**
```bash
# Jalankan file setup.bat
setup.bat
```

**Linux/Mac:**
```bash
# Berikan permission dan jalankan
chmod +x setup.sh
./setup.sh
```

### Opsi 2: Manual Setup

1. **Buat Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Aktifkan Virtual Environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Migrasi**
   ```bash
   python manage.py migrate
   ```

5. **Jalankan Server**
   ```bash
   python manage.py runserver
   ```

6. **Akses Aplikasi**
   - Buka browser: `http://127.0.0.1:8000`
   - Login dengan: `admin` / `admin123`

## 📱 Fitur yang Tersedia

### 1. Dashboard
- Statistik umum desa
- Grafik pertumbuhan penduduk
- Aktivitas terbaru
- Aksi cepat

### 2. Manajemen Penduduk
- Daftar penduduk dengan pencarian
- Filter berdasarkan status dan RT
- Tambah/edit data penduduk
- Detail penduduk lengkap

### 3. Manajemen Surat
- Statistik surat
- Daftar surat dengan status
- Buat surat baru
- Proses surat

### 4. Manajemen Keuangan
- Overview keuangan
- Grafik distribusi anggaran
- Tren keuangan
- Tabel transaksi

### 5. Pengaturan Profil
- Informasi personal
- Pengaturan keamanan
- Pengaturan notifikasi
- Log aktivitas

## 🎨 Desain Responsif

- **Desktop**: Sidebar + main content
- **Tablet**: Sidebar dapat dilipat
- **Mobile**: Sidebar overlay

## 🔧 Customisasi

### Mengubah Warna Tema
Edit file `static/css/admin.css`:
```css
:root {
    --primary-color: #2c3e50;    /* Warna utama */
    --secondary-color: #3498db;  /* Warna sekunder */
    --success-color: #27ae60;    /* Warna sukses */
    --warning-color: #f39c12;    /* Warna peringatan */
    --danger-color: #e74c3c;     /* Warna bahaya */
}
```

### Menambah Halaman Baru
1. Tambah URL di `admin_panel/urls.py`
2. Buat view function
3. Buat template di `templates/admin/`
4. Update navigasi di `base.html`

## 📊 Data Demo

Proyek ini menggunakan data placeholder untuk demonstrasi:
- **Penduduk**: 5 data sample
- **Surat**: 5 data sample
- **Keuangan**: 5 transaksi sample
- **Statistik**: Data dummy untuk grafik

## 🐛 Troubleshooting

### Error: Module not found
```bash
# Pastikan virtual environment aktif
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install ulang dependencies
pip install -r requirements.txt
```

### Error: Database not found
```bash
# Jalankan migrasi
python manage.py migrate
```

### Error: Static files not found
```bash
# Collect static files
python manage.py collectstatic
```

## 📞 Support

Jika ada masalah atau pertanyaan:
1. Periksa file README.md
2. Pastikan semua dependencies terinstall
3. Pastikan virtual environment aktif
4. Periksa log error di terminal

---

**Selamat mencoba Panel Admin Desa! 🎉**
