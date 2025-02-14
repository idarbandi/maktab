"""
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
"""

from django.db import models


class MaktabPosts(models.Model):
    """
    این مدل نمایانگر یک پست در برنامه مکتب است.
    """
    title = models.CharField(
        max_length=250)  # عنوان پست با حداکثر طول 250 کاراکتر
    content = models.TextField()  # محتوای پست

    def __str__(self):
        """
        بازگرداندن عنوان پست به عنوان نمایش رشته‌ای مدل
        """
        return self.title
