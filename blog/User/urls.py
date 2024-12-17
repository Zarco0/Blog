from django.urls import path
from .import views

app_name = 'webuser'

urlpatterns = [
    path('createblog/', views.createBlog, name='createblog'),
    path('viewblog/', views.viewBlog, name='viewblog'),
    path('userblogs/', views.viewUserBlog, name='viewuserblog'),
    path('detailblog/<int:blog_id>/',views.detailBlog,name='detailblog'),
    path('updateblog/<int:blog_id>/',views.updateBlog,name='updateblog'),
    path('deleteblog/<int:blog_id>/',views.deleteBlog,name='deleteblog'),
    path('update-profile/', views.updateProfile, name='updateprofile'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:blog_id>/comment/', views.add_comment, name='add_comment'),
]