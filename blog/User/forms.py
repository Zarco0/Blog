from django import forms
from .models import tbl_blog
from Authentication.models import tbl_userProfile

class BlogForm(forms.ModelForm):

    class Meta:

        model=tbl_blog
        fields=['title','content','image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog content here', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = tbl_userProfile
        fields = ['username', 'firstname', 'lastname', 'email', 'contactno', 'profilepic']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the first name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the email address'}),
            'contactno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the contact number'}),
            'profilepic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }