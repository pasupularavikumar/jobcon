from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT

# Create your models here.
class job(models.Model):
    JobTitle = models.CharField(max_length=200, null=True, blank=True)
    CompanyName = models.CharField(max_length=500,null=True,blank=True)
    salary = models.CharField(max_length=200, null=True,blank=True)
    NoOFOpenings = models.CharField(max_length=200, null=True,blank=True)
    workfromHome = models.BooleanField(default=False,null=True,blank=True)
    SkillsRequirement = models.CharField(max_length=1000,null=True)
    LocationCity = models.CharField(max_length=500, null=True,blank=True)
    EducationQualification = models.CharField(max_length=500, null=True,blank=True)
    EnglishLevel = models.CharField(max_length=500, null=True,blank=True)
    Experience = models.CharField(max_length=500, null=True,blank=True)
    desc1 = models.TextField(null=True,blank=True)
    Timings = models.CharField(max_length=500, null=True,blank=True)
    WorkingDays = models.CharField(max_length=500, null=True,blank=True)
    Address = models.CharField(max_length=500, null=True,blank=True)
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.JobTitle


class jobform(models.Model): 
    name = models.CharField(max_length=500, null=True, blank=True)
    phonenumber = models.CharField(max_length=500, null=True, blank=True)
    qualification = models.CharField(max_length=500, null=True, blank=True)
    Gender = models.CharField(max_length=50, null=True, blank=True)
    yearofpassing = models.CharField(max_length=500, null=True, blank=True)
    HigherEducation = models.CharField(max_length=500, null=True, blank=True)
    place = models.CharField(max_length=500, null=True, blank=True)
    Emailid = models.EmailField(max_length=500,blank=True, null=True)
    Resume = models.FileField(blank=True,null=True)
    form_time = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.name
class contactus(models.Model):
    firstName = models.CharField(max_length=500, null=True, blank=True)
    lastName = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=500,null=True,blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField(null=True,blank=True)
    CUs_Time = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.firstName

        
class Carousel(models.Model):
    image       = models.ImageField(upload_to="pics/%y/%m/%d/", null=True, blank=True)
    title       = models.CharField(max_length=500, null=True, blank=True)
    action_name = models.CharField(max_length=500, null=True, blank=True)
    link        = models.TextField(null=True, blank=True)
    sub_title   = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 