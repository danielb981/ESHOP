from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import


# Create your models here.

class Profile(models.Model):
    bio = models.TextField(null=True, blank=True)
    social_link = models.URLField(max_length=5000)
    phone_number = models.CharField(null=True, blank=True,max_length=100)
    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь"
    )

    def __str__(self):
        return self.bio

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    qty = models.IntegerField(default=0)
    costumer_views = models.ManyToManyField(
        to=costumer_views

    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Категория"
    )

    def __str__(self):
        return self.name