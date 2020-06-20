from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Create your models here.
class CustomUser(AbstractUser):
    telephone_numb = models.CharField(max_length=12, null=False, default="-", blank=True, unique=True)

    def __str__(self):
        """
        Возвращает строковое представление этого `User`.
        Эта строка используется, когда в консоли выводится `User`.
        """
        return self.username
