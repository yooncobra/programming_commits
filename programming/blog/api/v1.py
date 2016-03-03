from django.conf.urls import url
from django.http import JsonResponse
from blog.models import Post


def post_list(request):
    post_list = [post.title for post in Post.objects.all()]
    return JsonRespose(post_list, safe=False)


urlpatterns = [
        url(r'^posts/$', post_list),
        ]

