from django.contrib import admin

from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)


admin.site.register(Posts, PostsAdmin)
