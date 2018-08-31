from django.db import models

# Create your models here.
class BlogsPost(models.Model):
	title = models.CharField(max_length = 50)
	body = models.TextField()
	timestamp = models.DateTimeField()