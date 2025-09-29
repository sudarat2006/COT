from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_GET
from functools import lru_cache
import json
from pathlib import Path

# Create your views here.

def index(request):
    return render(request, 'index.html')


# Data loading and caching
CHERRY_JSON_PATH = Path(settings.BASE_DIR) / 'cherry.json' 
