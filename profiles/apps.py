"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.apps import AppConfig


class MaktabProfilesConfig(AppConfig):
    """
    تنظیمات اپلیکیشن پروفایل‌ها برای پروژه مکتب
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        """
        متد آماده‌سازی اپلیکیشن که سیگنال‌ها را وارد می‌کند
        """
        import profiles.signals
