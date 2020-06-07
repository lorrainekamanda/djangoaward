from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import registrationForm,UpdateUser,UpdateProfile,CommentForm
from django.contrib.auth.models import User
from .models import Image,Profile,Comments,Preference
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .serializer import ImageSerializer,ProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from rest_framework import status

def is_users(image_user, logged_user):
    return image_user == logged_user

class CreateDetail(LoginRequiredMixin,CreateView):
    model = Image
    fields = ['image','description','URL','sitename','category','tags','countries','twitter']
    

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class CreateComment(LoginRequiredMixin,CreateView):
    model = Comments
    fields = ['comments']
    
    template_name = 'blog/comment-detail.html'
    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class UpdateDetail(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Image
    fields = ['image','description','URL','sitename','category','tags','countries']
    def test_func(self):
        image = self.get_object()
        if self.request.user == image.username:
            return True
        return False


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class ImageView(LoginRequiredMixin,ListView):
    
    model = Image
   
    template_name = 'blog/home.html'
    context_object_name = 'images'

class CommentView(ListView):
    model = Comments
    template_name = 'blog/image-detail.html'
    context_object_name = 'comments'




        
    
   
def register(request):
    if request.method == 'POST':
       form = registrationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request,f'Account created for {username}')
           return redirect('blog-login')

    else:
       form = registrationForm()
    return render (request,'blog/register.html',{'form':form})


def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = Image.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'blog/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searches/search.html',{"message":message})

