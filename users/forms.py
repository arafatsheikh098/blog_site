from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# class UserSignupForms(forms.Form):
#     username=forms.CharField()
#     email=forms.EmailField()
#     password=forms.CharField()
#     cPassword=forms.CharField()

#     def clean_username(self):
#         username=self.cleaned_data["username"]
#         if User.objects.filter(username=username).exists:
#             raise forms.ValidationError("Username already exists")
#         return username
#     def clean_password(self):
#         password=self.cleaned_data["password"]
#         cPassword=self.cleaned_data["cPassword"]

#         if cPassword !=password:
#             raise forms.ValidationError("Password don't match")
#         return password

class UserSignupForms(UserCreationForm):
    class Meta :
        model=User
        fields=["username","email","password1","password2"]

  



