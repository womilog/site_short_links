from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Link(models.Model):
    full_url = models.URLField(max_length=250, blank=False)
    short_url = models.CharField(max_length=100, unique=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links', blank=False)

    def __str__(self):
        return self.short_url

    class Meta:
        verbose_name = 'ссылка'
        verbose_name_plural = 'ссылки'
