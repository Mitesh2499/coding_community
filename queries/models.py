from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from taggit.managers import TaggableManager
# Create your models here.

class ask_question(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=3000)

    description=RichTextField()
    image=models.FileField(null=True,blank=True,upload_to='Question')
    tags = TaggableManager()
    slug = models.SlugField(unique=True,max_length=100)
    created_date=models.DateTimeField(default=now)
    updated_date=models.DateTimeField(default=now)
    
    def __str__(self):
        return self.question

DISCUSSION=(
    ("question","question"),
    ("solution","solution")
)
class Dicussion_Like(models.Model):
    discussion=models.ForeignKey(ask_question,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #type=models.CharField(max_length=10, choices=DISCUSSION)
    date_upload=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("user", "discussion"),)
        ordering = ["-date_upload"]

class Solution(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(ask_question,on_delete=models.CASCADE)
    description=RichTextField()
    image=models.FileField(null=True,blank=True,upload_to='Question')
    created_date=models.DateTimeField(default=now)
    updated_date=models.DateTimeField(default=now)
    def __str__(self):
        return str(self.user)+" Gives answer to "+str(self.question)
    


class Solution_Like(models.Model):
    solution=models.ForeignKey(Solution,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #type=models.CharField(max_length=10, choices=DISCUSSION)
    date_upload=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("user", "solution"),)
        ordering = ["-date_upload"]