"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.db.models import Count, Q
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    MaktabComment,
    MaktabNotification,
    MaktabPost,
    MaktabUserProfile,
    User,
)
from .serializers import (
    MaktabCommentSerializer,
    MaktabNotificationSerializer,
    MaktabPostSerializer,
    MaktabUserProfileSerializer,
    MaktabUserSerializer,
)


class MaktabSearchView(generics.ListAPIView):
    """
    کلاس جستجو برای جستجوی پست‌ها و کاربران در پروژه مکتب
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        دریافت queryset برای جستجوی پست‌ها و کاربران
        """
        query = self.request.query_params.get('q', '')
        posts = MaktabPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query))
        users = User.objects.filter(
            Q(username__icontains=query) | Q(email__icontains=query))
        return {'posts': MaktabPostSerializer(posts, many=True).data,
                'users': MaktabUserSerializer(users, many=True).data}

    def list(self, request, *args, **kwargs):
        """
        لیست کردن نتایج جستجو
        """
        response = self.get_queryset()
        return Response(response)


class MaktabCommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet برای مدیریت کامنت‌ها در پروژه مکتب
    """
    queryset = MaktabComment.objects.all().order_by('-created_at')
    serializer_class = MaktabCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        ذخیره کامنت جدید با استفاده از کاربر جاری
        """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        دریافت queryset برای نمایش کامنت‌های پست خاص
        """
        post_id = self.request.query_params.get('post', None)
        if post_id is not None:
            return MaktabComment.objects.filter(post_id=post_id)
        return super().get_queryset()

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """
        لایک یا آنلایک کردن کامنت توسط کاربر
        """
        comment = self.get_object()
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        return Response({'status': 'like toggled', 'like_count': comment.like_count})


class MaktabUserProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet برای مدیریت پروفایل‌های کاربران در پروژه مکتب
    """
    queryset = MaktabUserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MaktabUserProfileSerializer

    def get_queryset(self):
        """
        دریافت queryset برای نمایش پروفایل کاربر جاری
        """
        return MaktabUserProfile.objects.filter(user=self.request.user)


class MaktabUserProfileUpdateView(APIView):
    """
    APIView برای به‌روزرسانی پروفایل کاربر در پروژه مکتب
    """
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        """
        به‌روزرسانی پروفایل کاربر با داده‌های جدید
        """
        user_profile = request.user.maktabuserprofile
        serializer = MaktabUserProfileSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class MaktabUserDetailView(APIView):
    """
    APIView برای نمایش جزئیات کاربر در پروژه مکتب
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        دریافت اطلاعات کاربر جاری
        """
        user = request.user
        serializer = MaktabUserSerializer(user)
        return Response(serializer.data)


class MaktabFilterSortPostView(generics.ListAPIView):
    """
    APIView برای فیلتر و مرتب‌سازی پست‌ها در پروژه مکتب
    """
    queryset = MaktabPost.objects.all()
    serializer_class = MaktabPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        دریافت queryset برای فیلتر و مرتب‌سازی پست‌ها
        """
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        tag = self.request.query_params.get('tag')
        sort_by = self.request.query_params.get('sort_by')

        if category:
            queryset = queryset.filter(categories__name=category)
        if tag:
            queryset = queryset.filter(tags__name=tag)
        if sort_by == 'popularity':
            queryset = queryset.annotate(
                like_count=Count('likes')).order_by('-like_count')
        elif sort_by == 'date':
            queryset = queryset.order_by('-created_at')

        return queryset


class MaktabUserDashboardView(APIView):
    """
    APIView برای نمایش داشبورد کاربر در پروژه مکتب
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        دریافت اطلاعات داشبورد کاربر جاری
        """
        user = request.user
        user_data = MaktabUserSerializer(user).data
        recent_posts = user.maktabposts.order_by('-created_at')[:5]
        notifications = user.maktabnotifications.order_by('-created_at')[:5]

        data = {
            'user': user_data,
            'recent_posts': MaktabPostSerializer(recent_posts, many=True).data,
            'notifications': MaktabNotificationSerializer(notifications, many=True).data
        }
        return Response(data)


class MaktabNotificationViewSet(viewsets.ModelViewSet):
    """
    ViewSet برای مدیریت نوتیفیکیشن‌ها در پروژه مکتب
    """
    queryset = MaktabNotification.objects.all().order_by('-created_at')
    serializer_class = MaktabNotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        دریافت queryset برای نمایش نوتیفیکیشن‌های کاربر جاری
        """
        user = self.request.user
        return MaktabNotification.objects.filter(user=user)


class MaktabIDAdminView(APIView):
    """
    APIView برای بررسی ادمین بودن کاربر در پروژه مکتب
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        بررسی و بازگرداندن پیام براساس وضعیت ادمین بودن کاربر
        """
        if request.user.is_superuser or request.user.is_staff:
            return Response({"message": "You are an admin"})
        else:
            return Response({"message": "You are not an admin"}, status=403)
