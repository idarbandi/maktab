# profiles/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Category, Comment, Notification, Post, Tag, UserProfile


# Custom UserAdmin to manage UserProfile
class UserProfileInline(admin.StackedInline):
    model: UserProfile
    can_delete: False


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = list(fieldsets)
            fieldsets.append(
                ('UserProfile', {'fields': ('bio', 'location', 'profile_picture')}))
        return fieldsets


# Register User model with custom UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'status')
    search_fields = ('title', 'user__username', 'content')
    list_filter = ('created_at', 'status')
    ordering = ('-created_at',)
    actions = ['approve_posts', 'reject_posts']

    def approve_posts(self, request, queryset):
        queryset.update(status='approved')
    approve_posts.short_description = 'Approve selected posts'

    def reject_posts(self, request, queryset):
        queryset.update(status='rejected')
    reject_posts.short_description = 'Reject selected posts'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at',
                    'content_excerpt', 'like_count')
    search_fields = ('user__username', 'post__title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def content_excerpt(self, obj):
        return obj.content[:50] + ('...' if len(obj.content) > 50 else '')
    content_excerpt.short_description = 'Content Excerpt'

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Like Count'


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message_excerpt', 'created_at', 'is_read')
    search_fields = ('user__username', 'message')
    list_filter = ('created_at', 'is_read')
    ordering = ('-created_at',)

    def message_excerpt(self, obj):
        return obj.message[:50] + ('...' if len(obj.message) > 50 else '')
    message_excerpt.short_description = 'Message Excerpt'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
