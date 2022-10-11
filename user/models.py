from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    #is_superuser = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username', 'password']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username