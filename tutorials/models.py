from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

import re
# Create your models here.
class Tutorial(models.Model):
    title=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.TextField()
    date_upload=models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorials")

    
class Like(models.Model):
    tutorial=models.ForeignKey(Tutorial,on_delete=models.CASCADE)
    userlike=models.ForeignKey(User,on_delete=models.CASCADE,related_name="tutorial_like")
    dateliked=models.DateTimeField(default=timezone.now)