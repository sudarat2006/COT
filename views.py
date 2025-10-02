from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_GET
from functools import lru_cache
import json
from pathlib import Path


# Create your views here.

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # ชื่อ login ต้องตรงกับ redirect('login')
]
# Data loading and caching
CHERRY_JSON_PATH = Path(settings.BASE_DIR) / 'cherry.json' 

