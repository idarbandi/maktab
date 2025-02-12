# profiles/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    FilterSortPostView,
    NotificationViewSet,
    SearchView,
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


# profiles/Search


router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='profile')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/details/', UserDetailView.as_view(), name='profile-details'),
    path('dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
    # Added this line for search
    path('search/', SearchView.as_view(), name='search'),
    path('posts/filter/', FilterSortPostView.as_view(), name='filter-sort-posts'),
]
