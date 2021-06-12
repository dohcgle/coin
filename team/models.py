from django.db import models

class Team(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    image = models.ImageField(upload_to='team/')
    is_active = models.BooleanField(default=True)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
