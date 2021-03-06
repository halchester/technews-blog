from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
STATUS = (0,"Draft"),(1,"Published")

class Post(models.Model):
    title = models.CharField(max_length = 50,unique = True)
    slug = models.SlugField(max_length = 50,unique = True)
    content = models.TextField(blank = False)
    author = models.ForeignKey(User,on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(choices = STATUS, default = 0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Commented on {} by {}'.format(self.created_on, self.name)
