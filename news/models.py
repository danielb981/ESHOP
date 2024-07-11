from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import news
# Create your models here.

class NewsCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    new = models.ForeignKey(
        to=news,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Категория"
    )
    def __str__(self):
        return self.name

class NEW(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField()
    views = models.IntegerField(default=0)
    user_views = models.ManyToManyField(
        to=User,
        blank=True,
    )

    def __str__(self):
        return self.title