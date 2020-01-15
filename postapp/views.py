from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import post,comment,like
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import CommentForm, PostForm
from ckeditor.widgets import CKEditorWidget
from django.views.decorators.csrf import csrf_exempt
from users.models import follow
# Create your views here.
class PostListView(ListView):
    model=post
    template_name='postapp/posts.html'
    context_object_name='posts'
    ordering=['-date_upload']

def postview(request):
    all_posts=post.objects.all()
    data=[]
    for post_instance in all_posts:
        likes=like.objects.filter(post=post_instance).count()
        commentscount=comment.objects.filter(post=post_instance).count()
        comments=comment.objects.filter(post=post_instance)
        is_liked=like.objects.filter(post=post_instance,user=request.user).count()
        user_liked=False
        if(is_liked==1):
            user_liked=True
       
        print(likes)
        print(commentscount,comments)

        data.append((post_instance,likes,commentscount,comments,user_liked))

    users=User.objects.all()
    followings=follow.objects.filter(follower=request.user)
    print("user",users)
    print("following",followings)

    following_list=[]
    for foll in followings:
        
        user_ins=get_object_or_404(User, username=foll.following)
       
        following_list.append(user_ins)

    print(following_list)
    not_follow=[]
   
    for user in users:
        if user not in following_list and user!=request.user :
            print("user",user)
            not_follow.append(user)
      
    
    context={"data":data,'users':not_follow}
    return render(request,'postapp/posts.html',context)

def single_post_view(request,post_id):
    post_instance= get_object_or_404(post, id=post_id)
    data=[]
    likes=like.objects.filter(post=post_instance).count()
    commentscount=comment.objects.filter(post=post_instance).count()
    comments=comment.objects.filter(post=post_instance)
    is_liked=like.objects.filter(post=post_instance,user=request.user).count()
    user_liked=False
    if(is_liked==1):
        user_liked=True
       
    print(likes)
    print(commentscount,comments)

    data.append((post_instance,likes,commentscount,comments,user_liked))

    context={"data":data}

    return render(request,'postapp/single_post_view.html',context)

def post_like(request,post_id=None):
    if request.method == 'GET':
        print("called functon")
     
        post_id=request.GET["post_id"]
          
        print(type)
        post_instance= get_object_or_404(post, id=post_id)
          
            #likedpost = post.objects.get(id = post_id )
        m = like(post=post_instance,user=request.user)
        m.save()
        likes=like.objects.filter(post=post_instance).count()
        
        return HttpResponse(likes)
       
    else:
        return HttpResponse("unsuccesful")

def follow_view(request):
    if request.method=="GET":
        follow_id=request.GET["user_id"]
        
        user_instance= get_object_or_404(User, id=follow_id)
        new_follow = follow.objects.create(follower=request.user, following=user_instance)
        return HttpResponse("true")

def unfollow_view(request):
    if request.method=="GET":
        follow_id=request.GET["user_id"]
        
        user_instance= get_object_or_404(User, id=follow_id)
        print(user_instance)
        print("user",request.user)
        new_follow = follow.objects.filter(follower=request.user, following=user_instance).delete()
        return HttpResponse("true") 



@csrf_exempt
def post_comment(request):
    pass

    if request.is_ajax():
        com=request.POST["comment"]
        
        print("ajax")
    else:
        print("not")
    return HttpResponse("ll")
        
    

'''


def postview(request):
    
    posts=post.objects.all()
    data={}
    for postid in posts:
        print(postid)
        likescount=like.objects.filter(post=postid).count()
   
        is_liked=like.objects.filter(post=postid,user=request.user).count()
        if is_liked==0:
            is_liked=False
        else:
            is_liked=True
        commentscount=comment.objects.filter(post=postid).count()
        comments=comment.objects.filter(post=postid)
        #post_likes.update({postid:{0:likescount,1:commentscount,2:comments}})
        data.update({postid : {"likescount":likescount,"comments":comments,"commentscount":commentscount,"is_liked":is_liked}})
    #postlikes=post_likes.items()
    posts=list(data.items())
    
    context={'posts':posts}

    
    return render(request,'postapp/posts.html',context)
   
#'
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
#'  
    #return render(request,'postapp/posts.html',{'posts':posts,'comments':comments,'comment_form':comment_form})
'''
class PostCreateView(LoginRequiredMixin,CreateView):
    model=post
    template_name='postapp/post_form.html'
    fields=['title','post','description']
  
    #form_class=PostForm
    #success_url=reverse_lazy('file-detail')
    def get_form(self, form_class=None):
        form = super(PostCreateView, self).get_form(form_class)
        form.fields['description'].widget = CKEditorWidget()
        return form

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


def liked(request,postid):
    try:
        postobj = get_object_or_404(post, id=postid)
        newlike = like.objects.create(user=request.user, post=postobj)
    except:
        pass
    return redirect(reverse('post-home'))

def likebtn(request):
    if request.method == 'GET':
        print("called functon")
        postid=request.GET["post_id"]
        post_id= get_object_or_404(post, id=postid)
        #likedpost = post.objects.get(id = post_id )
        m = like( post=post_id,user=request.user)
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

'''
def commented(request,postid):
    postobj = get_object_or_404(post, id=postid)
    commentobj=request.POST["comment"]
    newlike = comment.objects.create(user=request.user, post=postobj,comment_text=commentobj)
   
    

    return redirect(reverse('post-home'))
'''
@csrf_exempt
def commented(request,post_id=None):
    if request.method =="POST":
        post_id=request.POST["post_id"]

        print(post_id)
        postobj = get_object_or_404(post, id=post_id)
        
        commentobj=request.POST["comment"]
        new_comment = comment.objects.create(user=request.user, post=postobj,comment_text=commentobj)
        comments_count=comment.objects.filter(post=postobj).count()
        return HttpResponse(comments_count)
    return HttpResponse("false")
    
