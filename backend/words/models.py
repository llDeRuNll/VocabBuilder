from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Word(models.Model):
    en = models.CharField(max_length=100)
    ua = models.CharField(max_length=100)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

    is_irregular = models.BooleanField(default=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='words')

    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.en