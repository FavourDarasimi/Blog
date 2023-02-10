from django.urls import path,include
from .views import PostView,PostDetail,CreatePost,EditPost,DeletePost,AddComment
from . import views

urlpatterns =[   
    path('posts/',PostView.as_view(),name='posts'),
    path('post/detail/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('post/add/',CreatePost.as_view(),name='add_post'),
    path('post/edit/<int:pk>/',EditPost.as_view(),name='edit_post'),
    path('post/delete/<int:pk>/',DeletePost.as_view(),name='delete_post'),
    path('post/addcomment/<int:pk>/',AddComment.as_view(),name='add_comment'),
    path('like/<int:pk>',views.add_likes,name='like')
]