from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views import generic
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template = 'post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template = 'post_detail.html'
