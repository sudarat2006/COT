# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('delivery/', views.delivery, name='delivery'),
    path('track-order/', views.trackorder, name='trackorder'),  # ✅ เพิ่มบรรทัดนี้
]
