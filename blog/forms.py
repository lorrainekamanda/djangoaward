from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Image,Comments

class registrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    class Meta:

        model = User
        fields = ['username','email']
   
class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','phone_number','profile_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comments']

