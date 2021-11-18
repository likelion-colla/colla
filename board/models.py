from django.contrib.sites import requests
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to="board/image/%Y/%m/%d/%H",
        blank=True,
        null=True)
    # liked_users = models.ManyToManyField(TempUser, related_name="user_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"title : {self.title}"
