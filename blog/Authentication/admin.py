from django.contrib import admin
from .models import tbl_loginTable,tbl_userProfile

# Register your models here.

admin.site.register(tbl_userProfile)
admin.site.register(tbl_loginTable)