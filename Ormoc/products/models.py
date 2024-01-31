
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    # ... other fields ...

    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_permissions', blank=True
    )

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(null=True, blank=True,)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,)
    location = models.TextField(null=True,)
    price = models.TextField(null=True,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name