from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models import Q
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.
class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

class AwwwardsPost(models.Model):
    # id =
    title = models.CharField(max_length=150)
    image = CloudinaryField('image', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    country = models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now=True)
    project_link = models.URLField(max_length=300)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search(cls,searchterm):
        search = Post.objects.filter(Q(title__icontains=searchterm)|Q(description__icontains=searchterm)|Q(country__icontains=searchterm))
        return search
    
    
class Profile(models.Model):
    '''
    User profile model
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = CloudinaryField('image', blank=True, null=True)
    biography = HTMLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.biography

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_bio(cls,id, bio):
        update_profile = cls.objects.filter(id = id).update(bio = bio,)
        return update_profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
        
    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user__username__icontains=user).all()
    