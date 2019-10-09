from django.urls import path

from . import views
from .views import QuetionListView,IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    path('practice/', QuetionListView.as_view(), name='practice'),
    path('Compile/<int:pk>/', views.Compile, name='compile'),
    #path('', views.Compile, name='index')
    #path('file/<int:pk>/',PostDetailView.as_view(),name='file-detail' ),
 
    #path('AddQuestion/',views.Quetionview,name="addquestion")
    
]
