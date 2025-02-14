"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from rest_framework import serializers

from ..models import MaktabPosts  # تغییر نام مدل به شکل اختصاصی


class MaktabPostsSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل مدل پست‌ها به داده‌های JSON و بالعکس
    """

    class Meta:
        model = MaktabPosts  # مدل مورد استفاده در این Serializer
        fields = ['id', 'title', 'content']  # فیلدهای قابل نمایش و ویرایش
