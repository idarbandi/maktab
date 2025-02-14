"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from ..models import MaktabPosts  # تغییر نام مدل‌ها به شکل اختصاصی
# تغییر نام Serializer به شکل اختصاصی
from .serializers import MaktabPostsSerializer


class MaktabPostsViewSet(viewsets.ModelViewSet):
    """
    ViewSet برای مدیریت و نمایش پست‌های مکتب
    """
    queryset = MaktabPosts.objects.all()  # تعیین queryset برای نمایش همه پست‌ها
    serializer_class = MaktabPostsSerializer  # استفاده از Serializer اختصاصی
    # پشتیبانی از فیلتر و مرتب‌سازی
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # فیلتر کردن بر اساس دسته‌بندی و برچسب‌ها
    filterset_fields = ['category', 'tags']
    # مرتب‌سازی بر اساس تاریخ ایجاد و تعداد لایک‌ها
    ordering_fields = ['created_at', 'like_count']
    ordering = ['created_at']  # ترتیب پیش‌فرض بر اساس تاریخ ایجاد
