from django.contrib.auth.models import User

# dashboard/models.py
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    user = models.ForeignKey(
        User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
