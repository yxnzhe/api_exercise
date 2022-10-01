from email.utils import localtime
import secrets
from django.utils import timezone
from django.utils.timezone import timedelta
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    date_updated = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ForgotPassword(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    expire_at = models.DateTimeField(default=timezone.now() + timedelta(hours=24))
    is_redeemed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.id)