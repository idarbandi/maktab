"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MaktabPostsViewSet  # تغییر نام به شکل اختصاصی

# ایجاد یک نمونه از DefaultRouter برای مسیرهای API
router = DefaultRouter()
# ثبت مسیر posts با استفاده از ViewSet اختصاصی
router.register(r'posts', MaktabPostsViewSet)

urlpatterns = [
    path('', include(router.urls)),  # وارد کردن مسیرهای ایجاد شده توسط router
]
