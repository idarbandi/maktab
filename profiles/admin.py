# profiles/admin.py
from django.contrib import admin

from .models import Comment, Notification, Post, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
    search_fields = ('user__username', 'location')
    list_filter = ('location',)
    ordering = ('user',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


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
