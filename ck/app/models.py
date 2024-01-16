from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length = 50, blank = True, null = True, unique = False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Blog(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 50, blank = True)
    body = RichTextUploadingField(null=True, blank=True)
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
    def __str__(self):
        return self.name
 
class Ckeditor(models.Model):
    title = models.CharField(max_length = 50, blank = True)
    description = RichTextUploadingField(null=True, blank=True)
    class Meta:
        verbose_name = 'Ckeditor'
        verbose_name_plural = 'Ckeditors'
    
