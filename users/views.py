from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from users.forms import UserSignupForms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def signup_view(request):
    if request.method == "POST":
       form=UserSignupForms(request.POST)
       if form.is_valid():
    #         username=form.cleaned_data["username"]
    #         email=form.cleaned_data["email"]
    #         password=form.cleaned_data["password"]
            
            

    #     # username=request.POST.get("username")
    #     # email=request.POST.get("email")
    #     # password=request.POST.get("password")
    #     # confirmpassword=request.POST.get("cPassword")
    #         User.objects.create_user(username=username,email=email,password=password)
    #         return render(request,"login.html")
    #     else :
    #         return render(request, 'signup.html')
          form.save()
          return render(request,"login.html")
       context={"form":form}
       return render(request, 'signup.html',context)
    
    #    else :
    #       return render(request, 'signup.html')
          
    else :
       return render(request, 'signup.html')
       

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("post-list")  
        

        return render(request, "login.html", {"form": form})
    
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form}) 

       

          
    #  else :
    #     return render(request, 'signup.html')
def logout_view(request):
    logout(request)
    return redirect("login")

