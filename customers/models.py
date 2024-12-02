from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )
    loyalty_points = models.PositiveIntegerField(default=0)

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return f"{self.city}, {self.province}"
