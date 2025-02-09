# profiles/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserDetailView, UserProfileUpdateView, UserProfileViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/details/', UserDetailView.as_view(), name='profile-details'),
]
