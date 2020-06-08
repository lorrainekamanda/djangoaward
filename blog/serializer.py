from .models import Profile,Image
from rest_framework import serializers
from django.contrib.auth.models import User, Group

"""
serializers help convert data from django to json and vice versa
"""

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields =('bio','phone_number','profile_image')

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields =('URL','sitename','description','tags','technology','countries','category','image')

