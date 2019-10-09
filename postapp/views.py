from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import post,comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import CommentForm
# Create your views here.
class PostListView(ListView):
    model=post
    template_name='postapp/posts.html'
    context_object_name='posts'
    ordering=['-date_upload']
   
def postview(request):
    posts=post.objects.all()
    return render(request,'postapp/posts.html',{'posts':posts})
   
'''
    post_obj=get_object_or_404(1)
    comments=post_obj.comment.all()

    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post_obj
            new_comment.user=request.user
            new_comment.save()
        else:
            comment_form=CommentForm()
'''    
    #return render(request,'postapp/posts.html',{'posts':posts,'comments':comments,'comment_form':comment_form})
   
class PostCreateView(LoginRequiredMixin,CreateView):
    model=post
    template_name='postapp/post_form.html'
    fields=['title','post','description']
    #success_url=reverse_lazy('file-detail')

    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class UserPostListView(ListView):
    model=post
    template_name='postapp/user_posts.html'
    context_object_name='posts'
    ordering=['-date_upload']
    #paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
     
        
        return post.objects.filter(author=user).order_by('-date_upload')

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    template_name='postapp/post_form.html'
    fields=['title','post','description']

    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    success_url='/posts'
    template_name='postapp/post_confirm_delete.html'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
