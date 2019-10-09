from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ask_question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.TextField()
    code=models.TextField()
    image=models.FileField(null=True,blank=True,upload_to='Question')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)

class Solution(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(ask_question,on_delete=models.CASCADE)
    ans=models.TextField()
    code=models.TextField()
    image=models.FileField(null=True,blank=True,upload_to='Question')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)

