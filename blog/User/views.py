from django.shortcuts import render,redirect
from .models import tbl_blog,tbl_comments
from Authentication.models import tbl_loginTable,tbl_userProfile
from django.contrib import messages
from .forms import BlogForm,ProfileUpdateForm

# Create your views here.

def createBlog(request):

    username = request.session.get('username')

    if not username:
        messages.error(request, 'You need to log in first')
        return redirect('webAuth:login')
    
    try:
        user = tbl_loginTable.objects.get(username=username)
    except tbl_loginTable.DoesNotExist:
        messages.error(request, 'User not found')
        return redirect('webAuth:login')

    if request.method=='POST':

        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES.get('image')
        blog=tbl_blog(title=title,content=content,image=image,user=user)
        blog.save()
        return redirect('webuser:viewblog')
    
    return render(request,'User/blog.html')

def viewBlog(request):
    blogs=tbl_blog.objects.all()

    return render(request,'User/viewblog.html',{'blog':blogs})

def viewUserBlog(request):

    username = request.session.get('username')

    if not username:
        messages.error(request, 'You need to log in first')
        return redirect('webAuth:login')
    
    try:
        user = tbl_loginTable.objects.get(username=username)
    except tbl_loginTable.DoesNotExist:
        messages.error(request, 'User not found')
        return redirect('webAuth:login') 
    
    if not username:
        messages.error(request, 'You need to log in first')
        return redirect('webAuth:login')

    blogs=tbl_blog.objects.filter(user=user)

    return render(request,'User/userblogs.html',{'blogs':blogs})


def detailBlog(request,blog_id):
    blog=tbl_blog.objects.get(id=blog_id)

    return render(request,'User/detailblog.html',{'blog':blog})

def updateBlog(request,blog_id):
    blog=tbl_blog.objects.get(id=blog_id)

    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=blog)

        if form.is_valid:
            form.save()
            return redirect('webuser:viewuserblog')
    else:
        form=BlogForm(instance=blog)

    return render(request,'User/blogupdate.html',{'form':form})

def deleteBlog(request,blog_id):
    blog=tbl_blog.objects.get(id=blog_id)

    if request.method=='POST':
        blog.delete()
        return redirect('webuser:viewuserblog')
    
    return render(request,'User/blogupdate.html',{'blog':blog})

 

def updateProfile(request):
    username = request.session.get('username')

    if not username:
        messages.error(request, 'You need to log in first')
        return redirect('webAuth:login')

    try:
        user_profile = tbl_userProfile.objects.get(username=username)
        login_user = tbl_loginTable.objects.get(username=username)
    except (tbl_userProfile.DoesNotExist, tbl_loginTable.DoesNotExist):
        messages.error(request, 'User not found')
        return redirect('webAuth:login')

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            profile = form.save(commit=False)
            
            new_password = request.POST.get('password')
            if new_password:
                profile.password = new_password
                login_user.password = new_password
                login_user.save()

            profile.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('webuser:viewuserblog')
    else:
        form = ProfileUpdateForm(instance=user_profile)

    return render(request, 'User/updateprofile.html', {'form': form})



def add_comment(request, blog_id):
    blog = tbl_blog.objects.get(id=blog_id)
    
    if request.method == "POST":
        comment_text = request.POST['comment']
        username = request.session.get('username')
        if username:
            try:
                user = tbl_loginTable.objects.get(username=username)
            except tbl_loginTable.DoesNotExist:
                user = None
        else:
            user = None
        
        if user:
            comment = tbl_comments.objects.create(
                blog=blog,
                user=user,
                text=comment_text
            )
            return redirect('webuser:detailblog', blog_id=blog.id)
        else:
            return redirect('login') 
    
    return redirect('webuser:detailblog', blog_id=blog.id)


def blog_detail(request, blog_id):
    blog = tbl_blog.objects.get(id=blog_id)
    return render(request, 'User/detailblog.html', {'blog': blog})