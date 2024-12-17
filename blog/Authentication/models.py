from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class tbl_userProfile(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    profilepic = models.ImageField()
    contactno = models.IntegerField()
    password = models.CharField(max_length=255) 
    reset_code = models.CharField(max_length=8, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    login = models.OneToOneField('tbl_loginTable', on_delete=models.CASCADE, related_name='profile',null=True,)



    def __str__(self):
        return '{}'.format(self.username)
    
    def get_email_field_name(self):
        return 'email'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)  

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    
class tbl_loginTable(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.username)