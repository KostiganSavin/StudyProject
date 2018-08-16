from django.db import models

# Create your models here.

class Courses(models.Model):

    name = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=False, blank=True)