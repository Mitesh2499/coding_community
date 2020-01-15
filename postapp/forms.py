from django.forms import ModelForm, Textarea,Select,TextInput,HiddenInput
from django import forms
from .models import post,comment
from ckeditor_uploader.fields import RichTextUploadingFormField

class CommentForm(ModelForm):
    id=forms.CharField(widget=HiddenInput())
    class Meta:
        model = comment
        fields = ['id','comment_text']
        widgets = {
            'comment_text': TextInput(attrs={'class':'form-control','placeholder':'Add ur comment','style':'border-radius: 0'}),
            
        }
        
    

class PostForm(ModelForm):
    class Meta:
        model = post
        fields=['title','post','description']
  
        