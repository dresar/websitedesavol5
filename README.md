# Desa Admin Panel

Sistem Administrasi Desa Digital yang komprehensif untuk mengelola data penduduk, surat menyurat, keuangan, dan laporan desa.

## 🚀 Fitur Utama

### 📊 Dashboard
- Dashboard utama dengan statistik real-time
- Grafik dan chart interaktif
- Notifikasi sistem
- Quick access ke fitur utama

### 👥 Manajemen Penduduk
- Data penduduk lengkap (NIK, KK, dll)
- Manajemen keluarga
- Pencarian dan filter data
- Export/Import data penduduk
- Foto penduduk

### 📄 Surat Menyurat
- Jenis surat yang dapat dikustomisasi
- Template surat otomatis
- Tracking status surat
- Persyaratan surat
- Dokumen pendukung

### 💰 Manajemen Keuangan
- Pencatatan pemasukan dan pengeluaran
- Kategori transaksi
- Anggaran tahunan
- Saldo kas real-time
- Laporan keuangan

### 📈 Laporan & Monitoring
- Laporan periodik
- Export laporan (PDF, Excel, CSV)
- Monitoring sistem
- Audit log
- Backup otomatis

## 🛠️ Teknologi

- **Backend**: Django 4.2.7
- **Database**: PostgreSQL / SQLite
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Cache**: Redis
- **Web Server**: Nginx
- **Container**: Docker & Docker Compose
- **API**: Django REST Framework

## 📋 Prasyarat

- Python 3.11+
- PostgreSQL 15+ (opsional)
- Redis (opsional)
- Docker & Docker Compose (opsional)

## 🚀 Instalasi

### Metode 1: Docker (Recommended)

1. Clone repository:
```bash
git clone <repository-url>
cd websitedesapaneladmin
```

2. Jalankan dengan Docker Compose:
```bash
docker-compose up -d
```

3. Buat superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

4. Akses aplikasi di http://localhost

### Metode 2: Manual Installation

1. Clone repository:
```bash
git clone <repository-url>
cd websitedesapaneladmin
```

2. Buat virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup environment:
```bash
cp environment.env .env
# Edit .env sesuai kebutuhan
```

5. Jalankan migrasi:
```bash
python manage.py migrate
```

6. Buat superuser:
```bash
python manage.py createsuperuser
```

7. Jalankan server:
```bash
python manage.py runserver
```

8. Akses aplikasi di http://localhost:8000

## ⚙️ Konfigurasi

### Environment Variables

Buat file `.env` berdasarkan `environment.env`:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (untuk PostgreSQL)
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=admin_panel_db
DATABASE_USER=admin_panel_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Email Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database Configuration

#### SQLite (Default)
Tidak perlu konfigurasi tambahan, database akan dibuat otomatis.

#### PostgreSQL
1. Install PostgreSQL
2. Buat database dan user
3. Update environment variables
4. Jalankan migrasi

## 📱 API Documentation

### Authentication
```bash
# Login
POST /api/auth/login/
{
    "username": "admin",
    "password": "password"
}

# Logout
POST /api/auth/logout/
```

### Endpoints

#### Penduduk
- `GET /api/penduduk/` - List penduduk
- `POST /api/penduduk/` - Create penduduk
- `GET /api/penduduk/{id}/` - Detail penduduk
- `PUT /api/penduduk/{id}/` - Update penduduk
- `DELETE /api/penduduk/{id}/` - Delete penduduk

#### Surat
- `GET /api/surat/` - List surat
- `POST /api/surat/` - Create surat
- `GET /api/surat/{id}/` - Detail surat

#### Keuangan
- `GET /api/keuangan/pemasukan/` - List pemasukan
- `GET /api/keuangan/pengeluaran/` - List pengeluaran
- `GET /api/keuangan/saldo/` - Saldo kas

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.penduduk

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

## 📦 Deployment

### Production Settings

1. Update `DEBUG=False` di `.env`
2. Set `ALLOWED_HOSTS` dengan domain production
3. Konfigurasi database production
4. Setup SSL certificate
5. Konfigurasi email SMTP

### Docker Production

```bash
# Build production image
docker build -t desa-admin-panel .

# Run with production settings
docker run -d \
  -e DEBUG=False \
  -e DATABASE_URL=postgres://user:pass@host:port/db \
  -p 8000:8000 \
  desa-admin-panel
```

## 🔧 Development

### Code Style
```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8
```

### Database Migrations
```bash
# Create migration
python manage.py makemigrations

# Apply migration
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

## 📊 Monitoring

### Health Checks
- `/health/` - Basic health check
- `/admin/` - Django admin interface

### Logs
- Application logs: `logs/django.log`
- Nginx logs: `/var/log/nginx/`
- Docker logs: `docker-compose logs`

## 🤝 Contributing

1. Fork repository
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Support

- Email: support@desa-admin.com
- Documentation: [Wiki](https://github.com/your-repo/wiki)
- Issues: [GitHub Issues](https://github.com/your-repo/issues)

## 🎯 Roadmap

- [ ] Mobile app (React Native)
- [ ] Real-time notifications
- [ ] Advanced reporting
- [ ] Integration with external systems
- [ ] Multi-language support
- [ ] Advanced security features

## 📈 Changelog

### v1.0.0 (2024-01-13)
- Initial release
- Basic CRUD operations
- Admin interface
- Docker support
- API endpoints

---

**Dibuat dengan ❤️ untuk kemajuan desa digital Indonesia**