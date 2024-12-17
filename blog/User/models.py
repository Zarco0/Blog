from django.db import models
from Authentication.models import tbl_loginTable

# Create your models here.

class tbl_blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.ImageField(upload_to='blog_images/')
    user=models.ForeignKey('Authentication.tbl_loginTable',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return '{}'.format(self.title)
    
class tbl_comments(models.Model):
    blog = models.ForeignKey(tbl_blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_loginTable, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"
    
    def __str__(self):
        return '{}'.format(self.blog)
