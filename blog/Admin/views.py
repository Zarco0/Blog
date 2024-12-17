from django.shortcuts import render, redirect, get_object_or_404
from Authentication .models import tbl_userProfile,tbl_loginTable
from User .models import tbl_blog
from django.contrib import messages
from .utils import send_notification_email



def user_list(request):
    users = tbl_userProfile.objects.all()  
    return render(request, 'admin/user_list.html', {'users': users})


def delete_user(request, user_id):
    try:
        user = tbl_userProfile.objects.get(id=user_id)
        user.delete()
        messages.success(request, "User deleted successfully.")
    except tbl_userProfile.DoesNotExist:
        messages.error(request, "User not found.")
    return redirect('admin:user_list')

def block_or_unblock_user(request, user_id):
    user_login = get_object_or_404(tbl_loginTable, id=user_id)

    if user_login.is_blocked:
        user_login.is_blocked = False 
        status = "unblocked"
        subject = "Your account has been unblocked"
        message = f"Dear {user_login.username},\n\nYour account has been unblocked by the admin."
    else:
        user_login.is_blocked = True  
        status = "blocked"
        subject = "Your account has been blocked"
        message = f"Dear {user_login.username},\n\nYour account has been blocked by the admin."

    user_login.save()

    
    send_notification_email(subject, message, user_login.profile.email) 

   
    messages.success(request, f"User has been {status} and notified via email.")

    return redirect('admin:user_list')


def blog_list(request):
    blogs = tbl_blog.objects.all() 
    return render(request, 'admin/blog_list.html', {'blogs': blogs})


def delete_blog(request, blog_id):
    
    blog = get_object_or_404(tbl_blog, id=blog_id)
    login_table_user = blog.user 

    try:

        user_profile = login_table_user.profile 
    except tbl_userProfile.DoesNotExist:
        messages.error(request, "User profile for this blog does not exist.")
        return redirect('admin:blog_list')

    blog.delete()

    subject = "Your blog post has been deleted"
    message = "Dear {},\n\nYour blog post titled '{}' has been deleted by the admin.".format(
        user_profile.username, blog.title
    )
  
    send_notification_email(subject, message, user_profile.email)
    messages.success(request, "Blog post has been deleted and the user has been notified via email.")

    return redirect('admin:blog_list')
