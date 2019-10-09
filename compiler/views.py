from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from .models import MyCompiler,Question
from .forms import CompilerForm,QuestionForm

import requests
from django.views.generic import ListView,TemplateView

class IndexView(TemplateView):
    template_name='compiler/index.html'

class QuetionListView(ListView):
    model=Question
    template_name='compiler/practice.html'
    context_object_name='quetions'
    ordering=['-date_uploaded']
    

def Compile(request,pk):
    print("execute",pk)
    question=Question.objects.get(id=pk)
    print(request.method)
    if request.method =='POST':
        form=CompilerForm(request.POST)
        print("form")
        print(form.is_valid())

        print(form.errors)
        
        
        code=form.instance.code
        lang=form.instance.getlanguage()
        user_input=form.instance.getUserInput()
        #print(lan)
        
        url = "https://ide.geeksforgeeks.org/main.php"
        data = {
        'lang': lang,
        'code': code,
        'input': user_input,
        'save': True
    }  
        form.save()
        r = requests.post(url, data=data).json()
        

        code_output={
            'valid':r['valid'],
            'output':r['output'],
            'rntError':r['rntError'],
            'cmpError':r['cmpError']
        }
        print(code_output)
        context={'code_output':code_output,'form':form,'question':question}
        print('if')
    else:
        form=CompilerForm()
        context={'form':form,'question':question}
        print('else')

        

    
    
    return render(request, 'compiler/compiler.html', context)
       
     #print(form.instance.code)

     
    '''
        allcodes=MyCompiler.objects.order_by('id')
        total=len(allcodes)
        code=allcodes[total-1]
        print(code)
    '''
        




def Quetionview(request):
    if request.method =='POST':
        form=QuestionForm(request.POST)
        form.save(commit=False)
        #print(form)
        #print(request.user)
        form.instance.user=request.user
        print(form.instance.user)
        form.save(commit=True)
        context={'form':form}
    else:
        form=QuestionForm()
        context={'form':form}


    
    return render(request, 'compiler/AddQuestion.html',context )

