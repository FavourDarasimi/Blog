from django.db import models
from accounts.models import Profile
from django.urls import reverse



class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=25)
    body=models.TextField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField('auth.User',related_name='likes')

    def num_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title)
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})    

    def get_absolute_url(self):
        return reverse("posts", kwargs={'pk':self.pk})        

class Comment(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
    body=models.TextField(max_length=150)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.post.pk})    

    

# Create your models here.
