from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models import Q
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone
from django.dispatch  import receiver
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django_countries.fields import CountryField

# Create your models here.
# class MoringaMerch(models.Model):
#     name = models.CharField(max_length=40)
#     description = models.TextField()
#     price = models.DecimalField(decimal_places=2, max_digits=20)
    
    
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
    
    
class Projects(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    country = CountryField(blank_label='(select country)', default='Kenya')
    link = models.URLField()
    author_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank = True, null=True)

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.author} Post'

    class Meta:
        db_table = 'project'
        ordering = ['date_created']

    def delete_project(self):
        self.delete()

    @classmethod
    def search_projects(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    @classmethod
    def get_project(cls,id):
        try:
            project = Projects.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return Project
    
    
    

    