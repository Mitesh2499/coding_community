from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    link=models.CharField(max_length=500)
    description=models.TextField()
    image=models.FileField(null=True,blank=True,upload_to='Question')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
