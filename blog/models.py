from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    date = models.CharField(max_length=100)
    content = models.TextField()
    link = models.TextField()
    class Meta:
        app_label = 'blog'