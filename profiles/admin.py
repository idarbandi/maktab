"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import (
    MaktabCategory,
    MaktabComment,
    MaktabNotification,
    MaktabPost,
    MaktabTag,
    MaktabUserProfile,
)


class MaktabUserProfileInline(admin.StackedInline):
    """
    Inline برای مدیریت پروفایل کاربران
    """
    model = MaktabUserProfile
    can_delete = False


class MaktabUserAdmin(BaseUserAdmin):
    """
    مدیریت سفارشی کاربران
    """
    inlines = (MaktabUserProfileInline,)

    def get_fieldsets(self, request, obj=None):
        """
        دریافت و تنظیم بخش‌های نمایش فیلدها در پنل مدیریت
        """
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = list(fieldsets)
            fieldsets.append(
                ('پروفایل کاربر', {'fields': ('bio', 'location', 'profile_picture')}))
        return fieldsets


# ثبت مدل User با مدیریت سفارشی
admin.site.unregister(User)
admin.site.register(User, MaktabUserAdmin)


def maktab_safe_register(model, admin_class):
    """
    ثبت امن مدل‌ها در پنل مدیریت
    """
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass


@admin.register(MaktabPost)
class MaktabPostAdmin(admin.ModelAdmin):
    """
    تنظیمات مدل پست در پنل مدیریت
    """
    list_display = ('title', 'user', 'created_at', 'status')
    search_fields = ('title', 'user__username', 'content')
    list_filter = ('created_at', 'status')
    ordering = ('-created_at',)
    actions = ['approve_maktab_posts', 'reject_maktab_posts']

    def approve_maktab_posts(self, request, queryset):
        """
        تایید پست‌های انتخاب شده
        """
        queryset.update(status='approved')
    approve_maktab_posts.short_description = 'تایید پست‌های انتخاب شده'

    def reject_maktab_posts(self, request, queryset):
        """
        رد پست‌های انتخاب شده
        """
        queryset.update(status='rejected')
    reject_maktab_posts.short_description = 'رد پست‌های انتخاب شده'


@admin.register(MaktabComment)
class MaktabCommentAdmin(admin.ModelAdmin):
    """
    تنظیمات مدل کامنت در پنل مدیریت
    """
    list_display = ('user', 'post', 'created_at',
                    'content_excerpt', 'like_count')
    search_fields = ('user__username', 'post__title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def content_excerpt(self, obj):
        """
        بازگرداندن بخشی از محتوای کامنت
        """
        return obj.content[:50] + ('...' if len(obj.content) > 50 else '')
    content_excerpt.short_description = 'خلاصه محتوا'

    def like_count(self, obj):
        """
        شمارش تعداد لایک‌ها
        """
        return obj.likes.count()
    like_count.short_description = 'تعداد لایک‌ها'


@admin.register(MaktabNotification)
class MaktabNotificationAdmin(admin.ModelAdmin):
    """
    تنظیمات مدل نوتیفیکیشن در پنل مدیریت
    """
    list_display = ('user', 'message_excerpt', 'created_at', 'is_read')
    search_fields = ('user__username', 'message')
    list_filter = ('created_at', 'is_read')
    ordering = ('-created_at',)

    def message_excerpt(self, obj):
        """
        بازگرداندن بخشی از پیام نوتیفیکیشن
        """
        return obj.message[:50] + ('...' if len(obj.message) > 50 else '')
    message_excerpt.short_description = 'خلاصه پیام'


@admin.register(MaktabCategory)
class MaktabCategoryAdmin(admin.ModelAdmin):
    """
    تنظیمات مدل دسته‌بندی در پنل مدیریت
    """
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(MaktabTag)
class MaktabTagAdmin(admin.ModelAdmin):
    """
    تنظیمات مدل تگ در پنل مدیریت
    """
    list_display = ('name',)
    search_fields = ('name',)


# ثبت مدل‌ها با کلاس‌های مدیریت
maktab_safe_register(MaktabPost, MaktabPostAdmin)
maktab_safe_register(MaktabComment, MaktabCommentAdmin)
maktab_safe_register(MaktabNotification, MaktabNotificationAdmin)
maktab_safe_register(MaktabCategory, MaktabCategoryAdmin)
maktab_safe_register(MaktabTag, MaktabTagAdmin)
