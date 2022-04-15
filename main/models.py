from django.db import models
from django.utils import timezone



class Task(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', max_length=256)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    posted = models.DateTimeField(verbose_name='Posted', default=timezone.now,)
    deleted = models.DateTimeField(verbose_name='Deleted', blank=True, null=True)

    def __str__(self):
        return self.title




