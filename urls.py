from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# 👇 แก้ตรงนี้ให้ถูกกับชื่อแอปของคุณ (สมมุติชื่อแอปคือ main)
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# 👇 แสดง media และ static files ใน development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # ปลอดภัยกรณี STATICFILES_DIRS ไม่ได้ตั้งค่า
    if hasattr(settings, 'STATICFILES_DIRS') and settings.STATICFILES_DIRS:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    else:
        # fallback สำหรับ static root
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
