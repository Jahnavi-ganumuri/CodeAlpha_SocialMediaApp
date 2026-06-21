from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content=models.TextField()

    created=models.DateTimeField(
        auto_now_add=True
    )

    likes=models.ManyToManyField(
        User,
        related_name="likes",
        blank=True
    )


class Comment(models.Model):

    post=models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text=models.TextField()

    created=models.DateTimeField(
        auto_now_add=True
    )