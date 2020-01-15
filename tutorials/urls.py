from django.urls import path

from . import views
from django.conf import settings
from .views import TutorialListView,TutorialCreateView,TutorialUpdateView,UserTutorialsListView,TutorialDeleteView
from django.conf.urls.static import static

urlpatterns = [
    path('tutorials/',TutorialListView.as_view(),name='tutorials' ),
    path('like/',views.like,name='like' ),
   
    path('create_tutorials/',TutorialCreateView.as_view(),name='create_tutorials' ),
    path('tutorials/<int:pk>/update',TutorialUpdateView.as_view(),name='update_tutorials' ),
      path('tutorials/<int:pk>/delete',TutorialDeleteView.as_view(),name='delete_tutorials' ),
    
     path('user_tutorials/<str:username>',UserTutorialsListView.as_view(),name='user_tutorials' )
     
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)