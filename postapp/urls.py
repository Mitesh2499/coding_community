from django.urls import path

from . import views
from .views import postview ,PostListView,PostCreateView,UserPostListView,PostUpdateView,PostDeleteView,single_post_view,follow_view,unfollow_view,liked,commented,post_like,post_comment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('posts/',PostListView.as_view(),name='post-home' ),
    
    path('posts/',postview,name='post-home' ),
    path('posts/ajax/post_like/',post_like,name='post-like' ),
   path('userprofile/<int:post_id>/ajax/post_like/',post_like,name="single_post_like"),

    path('post_form/',PostCreateView.as_view(),name='post-form' ),
     path('user/<str:username>',UserPostListView.as_view(),name='user-post' ),
     path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update' ),
     path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete' ),
      path('posts/ajax/comment/',commented,name="post-comment"),
     path('userprofile/<int:post_id>/ajax/comment/',commented,name="single_post_comment"),

      path('post/ajax/follow/',follow_view,name="follow"),
       path('following/ajax/unfollow/',unfollow_view,name="unfollow"),
        path('userprofile/<int:post_id>/view',single_post_view,name="single_post_view")

  
     #path('like/',views.likebtn,name='like' ),
    #path('post/<int:postid>/like',liked,name='post-like' ),
    
    #path('post/<int:postid>/comment',commented,name='comment' ),
   
  
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)