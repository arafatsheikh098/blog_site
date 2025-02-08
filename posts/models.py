from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=60)
    content = models.TextField()
    publish_date= models.DateField()

class comment(models.Model):
    text = models.CharField(max_length=100)
     