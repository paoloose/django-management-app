from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=False)
    published = models.DateField(auto_now_add=True)
