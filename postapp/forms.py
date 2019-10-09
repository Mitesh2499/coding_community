from django.forms import ModelForm, Textarea,Select,TextInput
from .models import post,comment

class CommentForm(ModelForm):
    class Meta:
        model = comment
        fields = ['comment_text']
        widgets = {
            'comment_text': TextInput(attrs={'class':'form-control','placeholder':'Add ur comment','style':'border-radius: 0'}),
            
        }
        
    
