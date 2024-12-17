from django.shortcuts import render,redirect
from .models import tbl_userProfile,tbl_loginTable
from django.contrib import messages
from django.contrib.auth import logout

from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from .forms import ForgotPasswordForm

from django.contrib.auth import update_session_auth_hash
from .forms import SetPasswordForm


def userRegisration(request):

    if request.method == 'POST':
        if tbl_userProfile.objects.filter(username=request.POST['username']).exists():
            messages.info(request, 'Username already taken')
            return redirect('webAuth:register')

        if tbl_userProfile.objects.filter(email=request.POST['email']).exists():
            messages.info(request, 'Email already registered')
            return redirect('webAuth:register')

        logintable = tbl_loginTable()
        logintable.username = request.POST['username']
        logintable.password = request.POST['password']  # Make sure to hash the password
        logintable.type = 'user'
        logintable.save()

        userProfile = tbl_userProfile()
        userProfile.username = request.POST['username']
        userProfile.firstname = request.POST['fname']
        userProfile.lastname = request.POST['lname']
        userProfile.email = request.POST['email']
        userProfile.profilepic = request.FILES.get('profilepic')
        userProfile.contactno = request.POST.get('contactno')
        userProfile.password = request.POST['password'] 
        userProfile.login = logintable
        userProfile.save()

        messages.success(request, 'Registration successful')
        return redirect('webAuth:login')

    return render(request, 'Authentication/register.html')



def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = tbl_loginTable.objects.get(username=username, password=password)

            if user.is_blocked:
                messages.error(request, "Your account has been blocked. Please contact the administrator.")
                return redirect('webAuth:login')

            request.session['username'] = user.username

            if user.type == 'user':
                return redirect('webuser:createblog')  
            elif user.type == 'admin':
                return redirect('webadmin:dashboard')  
            else:
                messages.error(request, 'Invalid role')
        except tbl_loginTable.DoesNotExist:
            messages.error(request, 'Invalid Username or Password')

    return render(request, 'Authentication/login.html')


def logout_view(request):
    logout(request)
    return redirect('webAuth:login')



def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = tbl_userProfile.objects.get(email=email)
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(str(user.id).encode())

                domain = get_current_site(request).domain
                reset_link = f'http://{domain}/reset-password/{uid}/{token}/'

                send_mail(
                    'Password Reset Request',
                    f'Click the link to reset your password: {reset_link}',
                    'no-reply@yourdomain.com',
                    [email],
                )
                return redirect('webAuth:password_reset_done')
            except tbl_userProfile.DoesNotExist:
                form.add_error('email', 'No user is registered with this email.')
    else:
        form = ForgotPasswordForm()

    return render(request, 'Authentication/forgot_password.html', {'form': form})


def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = tbl_userProfile.objects.get(id=uid)

        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                new_password = request.POST['password']
                user.set_password(new_password) 
                user.save() 
                messages.success(request, 'Your password has been reset successfully!')
                return redirect('webAuth:password_reset_complete') 
            else:
                return render(request, 'Authentication/reset_password.html', {'user': user})

        else:
            messages.error(request, 'Invalid or expired reset link.')
            return redirect('webAuth:password_reset_invalid')
    except (TypeError, ValueError, OverflowError, tbl_userProfile.DoesNotExist):
        messages.error(request, 'Invalid password reset link.')
        return redirect('webAuth:password_reset_invalid')
    
def password_reset_done(request):
    return render(request, 'Authentication/password_reset_done.html')

def password_reset_complete(request):
    return render(request, 'Authentication/password_reset_complete.html')

def password_reset_invalid(request):
    return render(request, 'Authentication/password_reset_invalid.html')
