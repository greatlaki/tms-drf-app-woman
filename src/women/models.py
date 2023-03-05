from django.db import models

from categories.models import Category
from django_extended.models import BaseModel


class Women(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )
