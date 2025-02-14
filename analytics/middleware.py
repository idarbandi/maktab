"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class MaktabAnalyticsMiddleware:
    """
    Middleware برای پیگیری و ثبت اطلاعات درخواست‌های کاربر
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        مدیریت درخواست‌ها و ثبت لاگ‌های مربوط به کاربران
        """
        response = self.get_response(request)

        # بررسی اطلاعات کاربر و تعیین نام کاربر
        user = request.user if request.user else 'Anonymous'

        # ثبت اطلاعات درخواست در لاگ
        logger.info(
            f'User: {user}, Path: {request.path}, Method: {request.method}, Status: {response.status_code}')

        return response


class MaktabAdminCheckMiddleware(MiddlewareMixin):
    """
    Middleware برای بررسی و تعیین سطح دسترسی کاربران
    """

    def process_request(self, request):
        """
        پردازش درخواست برای تعیین سطح دسترسی مدیران
        """
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            # تعیین کاربر به عنوان مدیر
            request.is_admin = True
        else:
            # کاربر عادی بدون دسترسی مدیر
            request.is_admin = False
