from django.urls import path
from blog import views

urlpatterns = [
    path('Post/', views.PostList.as_view()),
    path('Post/<int:module1_id>/', views.PostDetail.as_view()),

    path('Comment/', views.CommentList.as_view()),
    path('Comment/<int:module2_id>/', views.CommentDetail.as_view()),
]