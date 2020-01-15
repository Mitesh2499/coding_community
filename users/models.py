from django.db import models
from django.contrib.auth.models import User

from compiler.models import Question

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    score=models.IntegerField(default=0)
    bio=models.CharField(max_length=400)
    
    def __str__(self):
        return f'{self.user.username} Profile'

   
class follow(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("follower", "following"),)