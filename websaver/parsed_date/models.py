# parsed_date/models.py
from django.db import models

# Create your models here.
class BlogData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title
