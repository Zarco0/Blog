from django.urls import path
from .import views

app_name='webAuth'

urlpatterns = [
    path('',views.userRegisration,name='register'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('reset-password-complete/', views.password_reset_complete, name='password_reset_complete'),
    path('reset-password-invalid/', views.password_reset_invalid, name='password_reset_invalid'),
    path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
]