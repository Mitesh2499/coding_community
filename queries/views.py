from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import ask_question,Solution,Dicussion_Like,Solution_Like
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ckeditor.widgets import CKEditorWidget
from django.http import HttpResponse
from .forms import SolutionForm,ask_question_Form
from django.template.defaultfilters import slugify
from taggit.models import Tag
import json
#import simplejson
# Create your views here.
class AskQuestionView(LoginRequiredMixin,CreateView):
    model=ask_question
    template_name='queries/ask_question_form.html'
    fields=['question','description','image','tags']
    success_url=reverse_lazy('discussion')
    def get_form(self, form_class=None):
        form = super(AskQuestionView, self).get_form(form_class)
        form.fields['description'].widget = CKEditorWidget()
        return form
    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class DiscussionListView(ListView):
    model=ask_question
    template_name='queries/discussion.html'
    context_object_name='queries'
    ordering=['-created_date']



def like_discussion(request):
    if request.method == 'GET':
        print("called functon")
     
        queryid=request.GET["query_id"]
          
        print(type)
        query= get_object_or_404(ask_question, id=queryid)
          
            #likedpost = post.objects.get(id = post_id )
        m = Dicussion_Like(discussion=query,user=request.user)
        m.save()
        likes=Dicussion_Like.objects.filter(discussion=query).count()
        
       
        return HttpResponse(likes)
       
    else:
        return HttpResponse("unsuccesful")




def like_solution(request):
    if request.method == 'GET':
        print("called functon")
        try:
            queryid=request.GET["query_id"]
        
            query= get_object_or_404(Solution, id=queryid)
          
            #likedpost = post.objects.get(id = post_id )
            m = Solution_Like(solution=query,user=request.user)
            m.save()
            likes=Solution_Like.objects.filter(solution=query).count()
            print(likes)
            return HttpResponse(likes)
        except:
            return HttpResponse("unsuccesful")
    else:
        return HttpResponse("unsuccesful")


def discussion_view(request):
    questions=ask_question.objects.all()
    queries=[]
    for question in questions:
        likes=Dicussion_Like.objects.filter(discussion=question).count()
        is_liked=Dicussion_Like.objects.filter(discussion=question,user=request.user).count()
        user_liked=False
        if(is_liked==1):
            user_liked=True
        print(question,likes)
        queries.append((question,likes,user_liked))
    print(questions[0].tags.all())
    #question_tag=questions.tags.all()
    #print(question_tag)
    tags=Tag.objects.all()
    context={'queries':queries,'tags':tags}
    return render(request, 'queries/discussion.html', context)



def tagged(request, slug):
    print("exe")
    tag = get_object_or_404(Tag, slug=slug)
    print("tag"+str(tag))
    tags=Tag.objects.all()
    # Filter posts by tag name  
    questions = ask_question.objects.filter(tags=tag)
    queries=[]
    for question in questions:
        likes=Dicussion_Like.objects.filter(discussion=question).count()
        is_liked=Dicussion_Like.objects.filter(discussion=question,user=request.user).count()
        user_liked=False
        if(is_liked==1):
            user_liked=True
        print(question,likes)
        queries.append((question,likes,user_liked))
    print("q"+str(questions))
    context = {
        'tags':tags,
        'queries':queries,
    }
    return render(request, 'queries/discussion.html', context)




def ask_question_view(request):
    if request.method =="POST":
        form=ask_question_Form(request.POST,request.FILES)
        form.instance.author=request.user
        
        
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.slug = slugify(newpost.question)
            newpost.save()
        # Without this next line the tags won't be saved.
            form.save_m2m()
            redirect("discussion")
            #print(form.instance.description)
            #print("abc"+str(form.instance.image))
            #form.save()
            
        
        else:
            pass
    else:
        form=ask_question_Form()
        
    context={'form':form}
    return render(request, 'queries/ask_question_form.html', context)



def Detail_descussion(request,query_id):
    ques=ask_question.objects.get(id=query_id)
    ques_like=Dicussion_Like.objects.filter(discussion=ques).count()
    solutions=Solution.objects.filter(question=ques)
    
    print(solutions)
    sols=[]
    
    for s in solutions:
        print(s)
        likes=Solution_Like.objects.filter(solution=s).count()
        print(s,likes)
        is_liked=Solution_Like.objects.filter(solution=s,user=request.user).count()
        user_liked=False
        if(is_liked==1):
            user_liked=True
        sols.append((s,likes,user_liked))
    
    print(ques)
    if request.method =="POST":
        form=SolutionForm(request.POST,request.FILES)
        form.instance.user=request.user
        form.instance.question=ques
        print(form.instance.user)
        print(form.instance.question)
        
        if form.is_valid():
            #print(form.instance.description)
            #print("abc"+str(form.instance.image))
            form.save()
        
        else:
            pass
    else:
        form=SolutionForm()
    context={'query':ques,'form':form,'solutions':sols,"ques_likes":ques_like}
    return render(request, 'queries/detail-discussion.html', context)


