"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.contrib import admin

from .models import MaktabPosts  # تغییر نام مدل‌ها به شکل اختصاصی


class MaktabPostsAdmin(admin.ModelAdmin):
    """
    تنظیمات مدل Post در پنل مدیریت جنگو
    """
    list_display = ('title', 'content')  # نمایش فیلدهای عنوان و محتوا
    search_fields = ('title',)  # فعال‌سازی جستجو بر اساس عنوان


# ثبت مدل Posts در پنل مدیریت با استفاده از تنظیمات اختصاصی
admin.site.register(MaktabPosts, MaktabPostsAdmin)
