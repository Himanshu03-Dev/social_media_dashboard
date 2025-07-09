from django.db import models
from django.contrib.auth.models import User

class SocialPost(models.Model):
    PLATFORM_CHOICES = (
        ('Twitter', 'Twitter'),
        ('Facebook', 'Facebook'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.platform} Post by {self.user.username}'
