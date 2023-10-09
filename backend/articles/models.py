from django.db import models

class Article(models.Model):
    """
    This model represents an Article. Articles support CRUD operations
    and are associated with its author, who derives from the User model.
    """
    title = models.CharField(max_length=128)
    content = models.TextField(blank=False)
    published = models.DateTimeField(auto_now_add=True)
