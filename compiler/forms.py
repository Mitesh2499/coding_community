from django.forms import ModelForm, Textarea,Select
from .models import MyCompiler,Question

class CompilerForm(ModelForm):
    class Meta:
        model = MyCompiler
        fields = ['code','user_input','language']
        widgets = {
            'code': Textarea(attrs={'cols': 80, 'rows': 20,'class':'form-control'}),
            'user_input': Textarea(attrs={'cols': 30, 'rows': 7,'placeholder':'Input Here','required':False}),

            'language':Select(attrs={'onchange':'getlang()'})
        }
        
    
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields=['title','que','input_format','output_format','constraint','sample_input','sample_output']
        widgets = {
            'title': Textarea(attrs={'cols': 80, 'rows': 2,'class':'form-control'}),
            'que': Textarea(attrs={'cols': 30, 'rows': 5,'class':'form-control'}),
            'input_format': Textarea(attrs={'cols': 30, 'rows': 5,'class':'form-control'}),
            'output_format': Textarea(attrs={'cols': 30, 'rows': 5,'class':'form-control'}),
            'constraint': Textarea(attrs={'cols': 30, 'rows': 5,'class':'form-control'}),
            'sample_input': Textarea(attrs={'cols': 30, 'rows': 5,'class':'form-control'}),
            'sample_output': Textarea(attrs={'cols': 30, 'rows': 5,'class':'form-control'}),

            'language':Select()
        }