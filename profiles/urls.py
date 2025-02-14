"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MaktabCommentViewSet  # تغییر نام به شکل اختصاصی
from .views import MaktabFilterSortPostView  # تغییر نام به شکل اختصاصی
from .views import MaktabNotificationViewSet  # تغییر نام به شکل اختصاصی
from .views import MaktabSearchView  # تغییر نام به شکل اختصاصی
from .views import MaktabUserDashboardView  # تغییر نام به شکل اختصاصی
from .views import MaktabUserDetailView  # تغییر نام به شکل اختصاصی
from .views import MaktabUserProfileUpdateView  # تغییر نام به شکل اختصاصی
from .views import MaktabUserProfileViewSet  # تغییر نام به شکل اختصاصی

router = DefaultRouter()
router.register(r'profiles', MaktabUserProfileViewSet, basename='profile')
router.register(r'notifications', MaktabNotificationViewSet,
                basename='notification')
router.register(r'comments', MaktabCommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),  # وارد کردن مسیرهای ایجاد شده توسط router
    path('profile/update/', MaktabUserProfileUpdateView.as_view(),
         name='profile-update'),
    path('profile/details/', MaktabUserDetailView.as_view(), name='profile-details'),
    path('dashboard/', MaktabUserDashboardView.as_view(), name='user-dashboard'),
    path('search/', MaktabSearchView.as_view(),
         name='search'),  # وارد کردن مسیر جستجو
    path('posts/filter/', MaktabFilterSortPostView.as_view(),
         name='filter-sort-posts'),  # وارد کردن مسیر فیلتر و مرتب‌سازی پست‌ها
]
