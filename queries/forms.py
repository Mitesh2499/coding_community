from django.forms import ModelForm, Textarea,Select
from .models import Solution,ask_question
from ckeditor.widgets import CKEditorWidget


class ask_question_Form(ModelForm):
    class Meta:
        model=ask_question
        fields=["question","description","image","tags"]
class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['description','image']
        widgets = {
            'description': CKEditorWidget()
        }
        