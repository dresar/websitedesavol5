// Main Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS Animation
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100
    });

    // Initialize theme
    initializeTheme();
    
    // Initialize typing animation
    initializeTypingAnimation();
    
    // Initialize counter animation
    initializeCounterAnimation();
    
    // Initialize hero chart
    initializeHeroChart();
    
    // Initialize login form
    initializeLoginForm();
    
    // Initialize quick actions
    initializeQuickActions();
    
    // Initialize weather widget
    initializeWeatherWidget();
    
    // Initialize notifications
    initializeNotifications();
});

// Theme Management
function initializeTheme() {
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const html = document.documentElement;
    
    // Load saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-bs-theme', savedTheme);
    updateThemeIcon(savedTheme);
    
    themeToggle.addEventListener('click', function() {
        const currentTheme = html.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        html.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
        
        // Add animation effect
        themeToggle.classList.add('animate-pulse');
        setTimeout(() => {
            themeToggle.classList.remove('animate-pulse');
        }, 1000);
    });
}

function updateThemeIcon(theme) {
    const themeIcon = document.getElementById('themeIcon');
    if (theme === 'light') {
        themeIcon.className = 'bi bi-moon-fill';
    } else {
        themeIcon.className = 'bi bi-sun-fill';
    }
}

// Typing Animation
function initializeTypingAnimation() {
    const typingText = document.getElementById('typingText');
    const texts = [
        'Sistem Manajemen Desa Modern',
        'Administrasi Digital Terintegrasi',
        'Solusi Terbaik untuk Desa',
        'Teknologi untuk Kemajuan Desa'
    ];
    
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    
    function typeText() {
        const currentText = texts[textIndex];
        
        if (isDeleting) {
            typingText.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingText.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
        }
        
        let typeSpeed = isDeleting ? 50 : 100;
        
        if (!isDeleting && charIndex === currentText.length) {
            typeSpeed = 2000;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
            typeSpeed = 500;
        }
        
        setTimeout(typeText, typeSpeed);
    }
    
    typeText();
}

// Counter Animation
function initializeCounterAnimation() {
    const counters = document.querySelectorAll('[data-count]');
    
    const animateCounter = (counter) => {
        const target = parseInt(counter.getAttribute('data-count'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;
        
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        updateCounter();
    };
    
    // Intersection Observer for counter animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    });
    
    counters.forEach(counter => {
        observer.observe(counter);
    });
}

// Hero Chart
function initializeHeroChart() {
    const ctx = document.getElementById('heroChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Penduduk Aktif', 'Penduduk Pending', 'Penduduk Nonaktif'],
            datasets: [{
                data: [1200, 200, 50],
                backgroundColor: [
                    'rgba(40, 167, 69, 0.8)',
                    'rgba(255, 193, 7, 0.8)',
                    'rgba(220, 53, 69, 0.8)'
                ],
                borderColor: [
                    'rgba(40, 167, 69, 1)',
                    'rgba(255, 193, 7, 1)',
                    'rgba(220, 53, 69, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: 'white',
                        font: {
                            size: 12
                        }
                    }
                }
            },
            animation: {
                animateRotate: true,
                duration: 2000
            }
        }
    });
}

// Login Form
function initializeLoginForm() {
    const loginForm = document.getElementById('loginForm');
    const togglePassword = document.getElementById('togglePassword');
    
    // Toggle password visibility
    togglePassword.addEventListener('click', function() {
        const passwordField = loginForm.querySelector('input[type="password"]');
        const icon = this.querySelector('i');
        
        if (passwordField.type === 'password') {
            passwordField.type = 'text';
            icon.className = 'bi bi-eye-slash';
        } else {
            passwordField.type = 'password';
            icon.className = 'bi bi-eye';
        }
    });
    
    // Form submission
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        
        // Show loading state
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Memproses...';
        submitBtn.disabled = true;
        
        // Simulate login process
        setTimeout(() => {
            // Show success message
            showNotification('Login berhasil! Mengarahkan ke dashboard...', 'success');
            
            // Redirect to dashboard
            setTimeout(() => {
                window.location.href = '/dashboard/';
            }, 1500);
        }, 2000);
    });
}

// Quick Actions
function initializeQuickActions() {
    // Add hover effects to quick action buttons
    const quickActionBtns = document.querySelectorAll('.quick-action-btn');
    
    quickActionBtns.forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.02)';
        });
        
        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

// Weather Widget
function initializeWeatherWidget() {
    // Simulate real-time weather updates
    setInterval(() => {
        const temperature = document.querySelector('.weather-widget h2');
        if (temperature) {
            const currentTemp = parseInt(temperature.textContent);
            const newTemp = currentTemp + (Math.random() - 0.5) * 2;
            temperature.textContent = Math.round(newTemp) + '°C';
        }
    }, 30000); // Update every 30 seconds
}

// Notifications
function initializeNotifications() {
    // Show welcome notification
    setTimeout(() => {
        showNotification('Selamat datang di Panel Admin Desa!', 'info');
    }, 2000);
    
    // Show system status
    setTimeout(() => {
        showNotification('Semua sistem berjalan normal', 'success');
    }, 5000);
}

// Utility Functions
function scrollToFeatures() {
    document.getElementById('features').scrollIntoView({
        behavior: 'smooth'
    });
}

function showLoginModal() {
    const modal = new bootstrap.Modal(document.getElementById('loginModal'));
    modal.show();
}

function navigateTo(page) {
    // Add loading animation
    showNotification(`Mengarahkan ke ${page}...`, 'info');
    
    setTimeout(() => {
        window.location.href = `/${page}/`;
    }, 1000);
}

function quickAction(action) {
    const actions = {
        'tambah-penduduk': () => {
            showNotification('Membuka form tambah penduduk...', 'info');
            setTimeout(() => window.location.href = '/penduduk/', 1000);
        },
        'buat-surat': () => {
            showNotification('Membuka form buat surat...', 'info');
            setTimeout(() => window.location.href = '/surat/', 1000);
        },
        'catat-transaksi': () => {
            showNotification('Membuka form transaksi...', 'info');
            setTimeout(() => window.location.href = '/keuangan/', 1000);
        },
        'generate-laporan': () => {
            showNotification('Membuka generator laporan...', 'info');
            setTimeout(() => window.location.href = '/laporan/', 1000);
        }
    };
    
    if (actions[action]) {
        actions[action]();
    }
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Feature Card Animations
document.addEventListener('DOMContentLoaded', function() {
    const featureCards = document.querySelectorAll('.feature-card');
    
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
            this.style.boxShadow = '0 20px 40px rgba(0, 0, 0, 0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)';
        });
    });
});

// Floating Elements Animation
document.addEventListener('DOMContentLoaded', function() {
    const floatingElements = document.querySelectorAll('.floating-element');
    
    floatingElements.forEach((element, index) => {
        element.style.animationDelay = `${index * 2}s`;
    });
});

// Smooth Scrolling for all links
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Add loading states to all buttons
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('button');
    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('btn-close')) {
                this.classList.add('animate-pulse');
                setTimeout(() => {
                    this.classList.remove('animate-pulse');
                }, 1000);
            }
        });
    });
});

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl + K for search
    if (e.ctrlKey && e.key === 'k') {
        e.preventDefault();
        showNotification('Fitur pencarian global akan segera tersedia!', 'info');
    }
    
    // Escape to close modals
    if (e.key === 'Escape') {
        const modals = document.querySelectorAll('.modal.show');
        modals.forEach(modal => {
            const bsModal = bootstrap.Modal.getInstance(modal);
            if (bsModal) {
                bsModal.hide();
            }
        });
    }
});

// Performance monitoring
window.addEventListener('load', function() {
    const loadTime = performance.now();
    console.log(`Page loaded in ${loadTime.toFixed(2)}ms`);
    
    if (loadTime > 3000) {
        showNotification('Halaman membutuhkan waktu loading yang cukup lama. Periksa koneksi internet Anda.', 'warning');
    }
});

// Service Worker registration (for PWA features)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
