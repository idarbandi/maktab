"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MaktabUserProfile  # تغییر نام مدل به شکل اختصاصی


@receiver(post_save, sender=User)
def create_maktab_user_profile(sender, instance, created, **kwargs):
    """
    ایجاد پروفایل کاربری مکتب بعد از ساختن یک کاربر جدید
    """
    if created:
        MaktabUserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_maktab_user_profile(sender, instance, **kwargs):
    """
    ذخیره پروفایل کاربری مکتب بعد از به‌روزرسانی یک کاربر
    """
    instance.maktabuserprofile.save()
