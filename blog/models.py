from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    published_date = models.DateTimeField()
    views = models.PositiveIntegerField(default=0)
    reading_minute = models.PositiveSmallIntegerField()
    content = models.TextField()
    tg_link = models.URLField()

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
