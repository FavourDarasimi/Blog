from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.urls import reverse_lazy,reverse
from django.shortcuts import get_object_or_404
from accounts.models import Profile


class PostView(ListView):
    model=Post
    template_name="posts/post_view.html"
    context_object_name='posts'


class PostDetail(DetailView):
    model=Post
    template_name="posts/post_detail_view.html"

class CreatePost(CreateView):
    model=Post
    template_name="posts/create_post.html"
    fields=("title","body")
    success_url=reverse_lazy('posts')

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class EditPost(UpdateView):
    model=Post
    template_name="posts/edit_post.html"
    fields=("title","body")
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk' : self.object.pk})

class DeletePost(DeleteView):
    model=Post    
    template_name="posts/delete_post.html"
    context_object_name='post'
    success_url=reverse_lazy('posts')

class AddComment(CreateView):
    model=Comment
    template_name="posts/add_comment.html"
    fields=("body",)
    

    def form_valid(self,form,*args,**kwargs):
        form.instance.author=self.request.user
        post=get_object_or_404(Post,pk=self.kwargs.get('pk'))
        form.instance.post=post
        return super().form_valid(form)    
        

def add_likes(request,*args,**kwargs):
    post=get_object_or_404(Post,pk=kwargs.get('pk'))
    post.likes.add(request.user)
    context={'post':post}
    return redirect('post_detail',pk=kwargs.get('pk'))
    return render(request,'templates/posts/like.html',context)


          

# Create your views here.
