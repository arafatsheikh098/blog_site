from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method == "POST":
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("cPassword")
        User.objects.create_user(username=username,email=email,password=password)
        return render(request,"login.html")
    else :
      return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')