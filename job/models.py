from email.policy import default
from random import choices
from django.db import models
from django.utils.text import slugify
from sqlalchemy import ForeignKey
from django.contrib.auth.models import User


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time', 'Part Time'),
)

def image_upload(instance, filename):
    imagename , extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)

# Create your models here.
class job(models.Model):
    owner = models.ForeignKey(User,related_name="job_owner",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # column
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    Image = models.ImageField(upload_to=image_upload)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
   
    def __str__(self) :
        return self.title   # return title in job admin panel
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args,**kwargs)
    
    

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
 
 
 
    
class Apply(models.Model):
    job = models.ForeignKey(job,related_name='apply_job',on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    upload_cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name