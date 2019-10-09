from django.urls import path

from . import views
from .views import postview ,PostListView,PostCreateView,UserPostListView,PostUpdateView,PostDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('posts/',PostListView.as_view(),name='post-home' ),
    path('posts/',postview,name='post-home' ),
    path('post_form/',PostCreateView.as_view(),name='post-form' ),
     path('user/<str:username>',UserPostListView.as_view(),name='user-post' ),
     path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update' ),
     path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete' ),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)