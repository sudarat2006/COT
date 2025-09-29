from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login'), name='index'),  # เปิดเว็บแล้วพาไป login

    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),

    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('delivery/', views.delivery, name='delivery'),
    path('trackorder/', views.trackorder, name='trackorder'),
    path('order-status/', views.order_status, name='order_status'),
]
