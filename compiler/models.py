from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
LANGUAGES = (
    ('python','python'),
    ('python3','python3'),
    ('c', 'c'),
    ('cpp','cpp'),
    ('java','java'),
    ('js','js'),
)
LEVEL=(
    ('easy','Easy'),
    ('medium','Medium'),
    ('hard','Hard')

)
class MyCompiler(models.Model):
    code=models.CharField(max_length=3000)
    user_input=models.CharField(max_length=300,default="",blank=True)
    date_upload=models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=10, choices=LANGUAGES, default='c')
    def __str__(self):
        return self.code
    
    def getlanguage(self):
        return self.language

    def getUserInput(self):
        return self.user_input

class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    valid_author=models.BooleanField(default=False)
    title=models.TextField()
    que=models.TextField()
    input_format = models.TextField()
    output_format=models.TextField()
    constraint=models.TextField()
    sample_input=models.TextField()
    sample_output=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
    date_uploaded=models.DateTimeField(default=timezone.now)
    marks=models.IntegerField(default=0)
    level=models.CharField(max_length=6, choices=LEVEL, default='easy')
 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("compile", kwargs={"pk": self.pk})
    


class Testcases(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    testinput=models.CharField(max_length=100)
    testoutput=models.CharField(max_length=100)
