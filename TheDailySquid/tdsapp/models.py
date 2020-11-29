from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_images')
    bio = models.TextField(max_length=500)

class Account(User):
    profile = models.OneToOneField(
        to=Profile,
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE)
    dob = models.DateTimeField()

class Article(models.Model):
    name = models.TextField(max_length=300)
    body = models.TextField()
    category = models.TextField(max_length=300)

class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
