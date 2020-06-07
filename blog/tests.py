from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Image,Profile
# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    """
    testing the instation of the image class
    """
    def setUp(self):
        self.profile= Profile(profile_image= 'profile.jpg', bio ='Love life', phone_number =7286889)
        self.new_image = Image(caption = 'Nice pic',likes=44,comments = 'great pic keep it up' )
        self.new_image.save()
        self.profile.save()
        self.new_user= User(username  = 'Lorraine', email = 'lorrainekamanda@gmail.com')
        self.new_user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        self.new_image.save_images()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_delete_image(self):
        self.new_image.save_images()
        images = Image.objects.all()
        self.new_image.delete_images()
        self.assertTrue(len(images) == 0)
    