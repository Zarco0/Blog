from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('block-unblock-user/<int:user_id>/', views.block_or_unblock_user, name='block_unblock_user'),

    path('blogs/', views.blog_list, name='blog_list'),
    path('delete-blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
