from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from config.abstract_models import UUIDMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, name, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not name:
            raise ValueError('The Name field must be set')
        user = self.model(username=username, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password=None, **extra_fields):
        user = self.create_user(username, name, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser, UUIDMixin):
    name = models.CharField(max_length=50, blank=False, null=False)
    token = models.CharField(max_length=255, unique=True, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
