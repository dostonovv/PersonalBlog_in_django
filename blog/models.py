from django.db import models
from django.db.models import TextField
from django.forms import CharField
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body1 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    img = models.ImageField(upload_to='post_images/' , blank=True , null=True)

    def __str__(self):
        return f"{self.title} --- time : {self.created_at.strftime('%Y-%m-%d %H:%M')}\n{self.img}"