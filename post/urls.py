from django.urls import path,include
from . import views
from django.conf.urls import url
from .views import AddPostView,HomeView,LikeView


urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    
    path('add-event/',AddPostView.as_view(), name = "add-event"),
    path('like/<int:pk>',LikeView,name='like-post'),
    path('likes/',views.getLikes,name='like-page'),
]
