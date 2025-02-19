from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/profile/img', 
                              default='static/profile/img/avatar.jpeg')
    date_of_birth = models.DateTimeField(null=True)
    bio = models.CharField(max_length=250)
    email = models.EmailField()
    git_link = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=50, default="" ,blank=True , null=True)
    def __str__(self):
        
        return str(self.user)



class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='static/project/img', 
                              default='static/project/img/avatar.jpeg')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    github_url = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Referee(models.Model):
    referee_img = models.ImageField(upload_to='static/referee/img', 
                                    default='static/referee/img/avatar.jpeg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    referee_name = models.CharField(max_length=50)
    referee_url = models.URLField()
    referee_descript = models.CharField(max_length=250)
    referee_contact = models.CharField(max_length=25)
    def __str__(self):
        return self.referee_name

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=50)
    institute_desc = models.CharField(max_length=250)
    role = models.CharField(max_length=50)
    date_started = models.DateField()
    date_ended = models.DateField()
    def __str__(self):
        return self.institute_name

class Expert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expert_field = models.CharField(max_length=10)
    def __str__(self):
        return self.expert_field

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    referre = models.ForeignKey(Referee, on_delete=models.CASCADE, null=True, blank=True, default='')
    edu_title = models.CharField(max_length=25, default='')
    edu_files = models.FileField(upload_to='static/edufiles')
    edu_description = models.CharField(max_length=250)
    def __str__(self):
        return self.edu_title


#Hiring models
class HireMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    you_name = models.CharField(max_length=25)
    country = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    salary = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateField()

class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    git_link = models.URLField()
    def __str__(self):
        return self.phone















