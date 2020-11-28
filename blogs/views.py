from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views import generic
from .forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template = 'post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template = 'post_detail.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    newComment = None

    if request.method() == "POST":
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            newComment = comment_form.save(commit=False)
            newComment.post = post
            newComment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post, 'comments': comments, 'newComment': newComment,'comment_form': comment_form})
