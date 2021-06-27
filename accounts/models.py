from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username
