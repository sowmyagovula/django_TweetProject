from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    posted_at = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='media/', blank=True, null = True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]} - {self.posted_at}"
