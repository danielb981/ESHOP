from django.db import models

# Create your models here.
class NEW(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title