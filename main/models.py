from django.db import models
from django.contrib.auth.models import AbstractUser
from .services import upload_avatar_path

# Create your models here.

class Author(AbstractUser):
    avatar = models.ImageField(
        upload_to=upload_avatar_path,
        default='user/defaultuser/defaultuser.png'
    )

    def __str__(self):
        return self.username


class Book(models.Model):
    author = models.ManyToManyField(Author)
    name = models.CharField(max_length=150, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name