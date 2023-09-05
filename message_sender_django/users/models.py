from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from config.abstract_models import UUIDMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(username=username, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser, UUIDMixin):
    first_name = models.CharField(max_length=150)
    token = models.CharField(max_length=255, unique=True, null=True, blank=True)

    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
