"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.contrib.auth.models import User
from django.db import models


class MaktabUserProfile(models.Model):
    """
    پروفایل کاربر که شامل اطلاعات کاربری اضافی مانند بیوگرافی، مکان و تصویر پروفایل است.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True)

    def __str__(self):
        """
        بازگرداندن نام کاربری به عنوان نمایش رشته‌ای مدل پروفایل کاربر
        """
        return self.user.username


class MaktabCategory(models.Model):
    """
    مدل دسته‌بندی که شامل نام دسته‌بندی است.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        بازگرداندن نام دسته‌بندی به عنوان نمایش رشته‌ای مدل
        """
        return self.name


class MaktabTag(models.Model):
    """
    مدل تگ که شامل نام تگ است.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        بازگرداندن نام تگ به عنوان نمایش رشته‌ای مدل
        """
        return self.name


class MaktabPost(models.Model):
    """
    مدل پست که شامل عنوان، محتوا، تاریخ ایجاد، دسته‌بندی‌ها، تگ‌ها و وضعیت پست است.
    """
    STATUS_CHOICES = (
        ('pending', 'در انتظار'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(MaktabCategory, related_name='posts')
    tags = models.ManyToManyField(MaktabTag, related_name='posts')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        """
        بازگرداندن عنوان پست به عنوان نمایش رشته‌ای مدل
        """
        return self.title

    @property
    def like_count(self):
        """
        شمارش تعداد لایک‌های پست
        """
        return self.likes.count()


class MaktabNotification(models.Model):
    """
    مدل نوتیفیکیشن که شامل پیام‌های اعلان برای کاربر است.
    """
    NOTIFICATION_TYPES = (
        ('new_post', 'پست جدید'),
        ('comment', 'کامنت'),
        ('like', 'لایک'),
        ('follow', 'دنبال کردن'),
    )

    user = models.ForeignKey(
        User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(
        max_length=20, choices=NOTIFICATION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        """
        بازگرداندن بخشی از پیام نوتیفیکیشن به عنوان نمایش رشته‌ای مدل
        """
        return self.message[:50]


class MaktabComment(models.Model):
    """
    مدل کامنت که شامل محتوای کامنت‌ها و پاسخ‌ها به پست‌ها است.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        MaktabPost, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='comment_likes', blank=True)

    def __str__(self):
        """
        بازگرداندن نام کاربر و عنوان پست به عنوان نمایش رشته‌ای مدل کامنت
        """
        return f'کامنت از {self.user.username} روی {self.post.title}'

    @property
    def like_count(self):
        """
        شمارش تعداد لایک‌های کامنت
        """
        return self.likes.count()
