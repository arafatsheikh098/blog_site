from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=60)
    content = models.TextField()
    publish_date= models.DateField()

class comment(models.Model):
    text = models.CharField(max_length=100)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
