"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    MaktabCategory,
    MaktabComment,
    MaktabNotification,
    MaktabPost,
    MaktabTag,
    MaktabUserProfile,
)


class MaktabCommentSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل مدل کامنت‌ها به داده‌های JSON و بالعکس
    """
    replies = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = MaktabComment  # مدل مورد استفاده در این Serializer
        fields = '__all__'  # فیلدهای قابل نمایش و ویرایش

    def get_replies(self, obj):
        """
        دریافت کامنت‌های پاسخ داده شده به این کامنت
        """
        if obj.replies.exists():
            return MaktabCommentSerializer(obj.replies.all(), many=True).data
        return []


class MaktabCategorySerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل مدل دسته‌بندی‌ها به داده‌های JSON و بالعکس
    """
    class Meta:
        model = MaktabCategory  # مدل مورد استفاده در این Serializer
        fields = '__all__'  # فیلدهای قابل نمایش و ویرایش


class MaktabTagSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل مدل تگ‌ها به داده‌های JSON و بالعکس
    """
    class Meta:
        model = MaktabTag  # مدل مورد استفاده در این Serializer
        fields = '__all__'  # فیلدهای قابل نمایش و ویرایش


class MaktabPostSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل مدل پست‌ها به داده‌های JSON و بالعکس
    """
    categories = MaktabCategorySerializer(many=True, read_only=True)
    tags = MaktabTagSerializer(many=True, read_only=True)
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = MaktabPost  # مدل مورد استفاده در این Serializer
        fields = ['id', 'user', 'title', 'content', 'created_at',
                  'status', 'categories', 'tags', 'like_count']


class MaktabNotificationSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل مدل نوتیفیکیشن‌ها به داده‌های JSON و بالعکس
    """
    class Meta:
        model = MaktabNotification  # مدل مورد استفاده در این Serializer
        fields = ['id', 'message', 'created_at']  # فیلدهای قابل نمایش و ویرایش


class MaktabUserSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل مدل کاربران به داده‌های JSON و بالعکس
    """
    class Meta:
        model = User  # مدل مورد استفاده در این Serializer
        fields = ('id', 'username', 'email', 'is_superuser',
                  'is_staff')  # فیلدهای قابل نمایش و ویرایش


class MaktabUserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل مدل پروفایل کاربران به داده‌های JSON و بالعکس
    """
    user = MaktabUserSerializer(read_only=True)

    class Meta:
        model = MaktabUserProfile  # مدل مورد استفاده در این Serializer
        # فیلدهای قابل نمایش و ویرایش
        fields = ['user', 'bio', 'location', 'profile_picture']
