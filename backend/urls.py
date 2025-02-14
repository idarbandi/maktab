"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # مسیر مدیریت جنگو
    # وارد کردن مسیرهای مربوط به اپلیکیشن API
    path("api/", include('app.api.urls')),
    # وارد کردن مسیرهای مربوط به پروفایل‌ها
    path("profile/", include('profiles.urls')),
    # مسیرهای احراز هویت فریمورک REST
    path('api-auth/', include('rest_framework.urls')),
    # مسیرهای احراز هویت dj-rest-auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # مسیرهای ثبت‌نام dj-rest-auth
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # مسیرهای بازنشانی رمز عبور dj-rest-auth
    path('dj-rest-auth/password/reset/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),  # مسیرهای احراز هویت allauth
]
