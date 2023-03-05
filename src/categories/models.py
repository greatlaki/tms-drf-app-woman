from django.db import models

from django_extended.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
