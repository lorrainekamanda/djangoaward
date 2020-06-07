from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from django_countries.fields import CountryField    
# Create your models here.


        
class Profile(models.Model):

    profile_image = models.ImageField(default = 'profile.jpg',upload_to = 'images/')
    bio = models.TextField(max_length =160,null = True)
    phone_number = models.IntegerField(null = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE,null = True)
    
   

    def __str__(self):
        return self.user.username

class Image(models.Model):

    URL = models.URLField(null = True)
    twitter = models.URLField(null = True)
    image = models.ImageField(upload_to = 'images/')
    sitename = models.CharField(max_length =160,null = True)
    description = models.TextField(max_length =960,null = True)
    category = models.CharField(max_length =160,null = True)
    tags = models.CharField(max_length =160,null = True)
    technology = models.CharField(max_length =160,null = True)
    countries = CountryField(blank_label='(select country)')
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null = True)
    username= models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    date_posted = models.DateTimeField(default=timezone.now)
    @property
    def number_of_comments(self):
        return Comments.objects.filter(image=self).count()
    @classmethod
    def get_comments(cls,image_id):

       image = Image.objects.get(pk = image_id)
       image_comments = image.comments.set_all()
       return image_comments


    def get_absolute_url(self):
        return reverse ('image-detail', kwargs = {'pk':self.pk})
   

    @classmethod
    def search_by_username(cls,search_term):
        uses = cls.objects.filter(username__username__icontains=search_term)
        return uses

    def get_image_by_id(id):
        image = Image.objects.get(id = image_id)
        return image
    
    def save_images(self):
        self.save()
   
    def delete_images(self):
        self.delete()

  
    def __str__(self):
        return self.username.username

class Comments(models.Model):
    comments = models.TextField(max_length =1160,null = True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null = True)
    likes = models.IntegerField(default=0)
    username= models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null = True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse ('blog-home')

    def __str__(self):
        return self.username.username


class Preference(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    image= models.ForeignKey(Image, on_delete=models.CASCADE,null = True)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user) + ':' + str(self.image) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "image", "value")