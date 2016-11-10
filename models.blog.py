from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


"""
models.CharField -- текстовое поле с ограничением на количество символов. (Обязательный атрибус max_length=int)
models.TextField -- поле для неограниченно длинного текста. 
models.DateTimeField -- дата и время.
models.ForeignKey -- ссылка на другую модель.
"""