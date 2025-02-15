from django.db import models

# Create your models here.
class Note (models.Model) :
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return self.title
