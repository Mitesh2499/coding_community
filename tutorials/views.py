
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Tutorial
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
class TutorialListView(ListView):
    model=Tutorial
    template_name='tutorials/tutorials.html'
    context_object_name='tutorials'
    


   
class TutorialCreateView(LoginRequiredMixin,CreateView):
    model=Tutorial
    template_name='tutorials/tutorial_form.html'
    fields=['title','link','desc']
    #success_url=reverse_lazy('file-detail')

    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    
class TutorialUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Tutorial
    template_name='tutorials/tutorial_form.html'
    fields=['title','link','desc']

    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def test_func(self):
        file=self.get_object()
        if self.request.user == file.author:
            return True
        return False

class UserTutorialsListView(ListView):
    model=Tutorial
    template_name='tutorials/user_tutorials.html'
    context_object_name='tutorials'
    ordering=['-date_upload']
    #paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
     
        
        return Tutorial.objects.filter(author=user).order_by('-date_upload')

class TutorialDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Tutorial
    success_url='/tutorials'
    template_name='tutorials/tutorial_confirm_delete.html'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False