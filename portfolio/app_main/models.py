from django.db import models

# Create your models here.
class Home(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    designation=models.CharField(max_length=50,null=True,blank=True)
    full_designation=models.CharField(max_length=50,null=True,blank=True)
    picture=models.ImageField(upload_to='profile-picture',null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
#about section
class About(models.Model):
    heading=models.CharField(max_length=250,blank=True,null=True)
    career = models.CharField(max_length=250,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    profile_img=models.ImageField(upload_to='profile',blank=True,null=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Portfolio(models.Model):
    image=models.ImageField(upload_to='portfolio/',blank=True,null=True)
    link=models.URLField(max_length=200,blank=True,null=True)