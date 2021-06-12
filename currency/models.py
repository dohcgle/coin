from django.db import models

class Currency(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    content = models.TextField()
    slug = models.SlugField(max_length=255, verbose_name='slug', unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', unique=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
