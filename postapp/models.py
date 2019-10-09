from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=100)
    post=models.FileField(null=True,blank=True,upload_to='Files')
    description=models.TextField()
    date_upload=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-home")
  
class comment(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text=models.CharField(max_length=300)
    date_upload=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('date_upload',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user,self.post)

class like(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE,related_name='likes')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_upload=models.DateTimeField(auto_now_add=True)