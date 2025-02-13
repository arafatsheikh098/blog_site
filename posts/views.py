from django.shortcuts import render
from posts.models import Post
# Create your views here.
def post_list_view(request):
    post_data = Post.objects.all().order_by("id")
    context = {
        "data":post_data
    }

    return render(request,"post_list.html",context)