from django.shortcuts import render
from blog.models import Post


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    post_list = Post.objects.all()
    params = {'post_list': post_list}
    return render(request, 'blog/post_list.html', params)

