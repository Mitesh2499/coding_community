from django.urls import path

from . import views
from .views import AskQuestionView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #path('ask-question/',AskQuestionView.as_view(),name='ask-question' ),
    path('ask-question/',views.ask_question_view,name='ask-question' ),
    #path('discussion/',views.DiscussionListView.as_view(),name='discussion' ),
    path('discussion/',views.discussion_view,name='discussion' ),
    path('discussion-tag/<str:slug>',views.tagged,name='discussion-tag' ),
    path('discussion/ajax/like/',views.like_discussion,name='like-discussion' ),
    path('detail-discussion/ajax/like/',views.like_solution,name='like-solution' ),
    path('detail-discussion/<int:query_id>',views.Detail_descussion,name='detail_discussion' )
   
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)