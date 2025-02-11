# profiles/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    NotificationViewSet,
    UserDashboardView,
    UserDetailView,
    UserProfileUpdateView,
    UserProfileViewSet,
)

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='profile')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/details/', UserDetailView.as_view(), name='profile-details'),
    path('dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
]
