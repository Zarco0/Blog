from django.contrib import admin

from .models import tbl_blog,tbl_comments

# Register your models here.

admin.site.register(tbl_blog)
admin.site.register(tbl_comments)