from django.db import models

# Create your models here.
class Note (models.Model) :
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=10)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True) #自動加入筆記創建的時間

    def __str__(self):
        return self.title
