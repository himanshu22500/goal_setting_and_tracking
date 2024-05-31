from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.CharField(primary_key=True, default=uuid4, max_length=255)
    profile_pic_url = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
