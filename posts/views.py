from django.shortcuts import get_object_or_404, render
from posts.models import Post,comment
from django.views.generic import ListView
# Create your views here.
class postlist(ListView):
    template_name = "post_list.html"
    queryset= Post.objects.all()
    # html e data er place e object_list hobe 
def post_list_view(request):
    post_data = Post.objects.all().order_by("id")
    context = {
        "data":post_data
    }

    return render(request,"post_list.html",context)
def portfolio_view(request):
    portfolio_data= Post.objects.all().order_by('-id')[:3]

    context={
        "data":portfolio_data
    }
    return render(request,"portfolio.html",context)
def single_post_view(request,id):
    # single_post_data=Post.objects.get(id=id)
    single_post_data=get_object_or_404(Post,id=id)
    # try:
    #     single_post_data=Post.objects.get(id=id)
    # except obje

    single_post_comment=comment.objects.filter(post_id=id).select_related("user")
    context={
        "post":single_post_data,
        "comment":single_post_comment
    }
    return render(request,"single_post.html",context)
def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')