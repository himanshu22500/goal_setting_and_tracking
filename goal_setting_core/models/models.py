from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Goal(models.Model):
    id = models.CharField(primary_key=True, default=uuid4, max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="goals"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="goals",
    )
    target_datetime = models.DateTimeField()
    due_datetime = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(
        choices=[(1, "Low"), (2, "Medium"), (3, "High")], default=2
    )
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class GoalUpdate(models.Model):
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name="updates"
    )
    update_text = models.TextField()
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.goal.title} - {self.update_date}"
