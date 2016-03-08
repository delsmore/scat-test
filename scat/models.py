import uuid
from django.db import models
from django.utils import timezone
from time import time


	
def only_filename(instance, filename):
    return filename
    
class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=140, default=None, blank=True, null=True)
    image = models.FileField(upload_to=only_filename,default=None, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
         ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=200)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default=None, blank=True, null=True)
    summary = models.CharField(max_length=140, default=None, blank=True, null=True)
    image = models.FileField(upload_to=only_filename,default=None, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name_plural = "categories"

		
class Type(models.Model):
    type = models.CharField(max_length=100,  blank=True, null=True)
    def __str__(self):
        return self.type

class Provider(models.Model):
    college = models.CharField(max_length=50)
    school = models.CharField(max_length=150)
    def __str__(self):
        return self.college + ' - ' + self.school
    class Meta:
         ordering = ['college','school']

class People(models.Model):
    uun = models.CharField(max_length=8,default=None, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default=None, blank=True, null=True)
    telephone = models.CharField(max_length=50,default=None, blank=True, null=True)
    department = models.CharField(max_length=100,default=None, blank=True, null=True)
    image = models.FileField(upload_to=only_filename,default=None, blank=True, null=True)
    def __str__(self):
        return self.name
   
    class Meta:
        ordering = ['name']
        verbose_name_plural = "people"
        
class Status(models.Model):
    stage = models.CharField(max_length=50)
    def __str__(self):
        return self.stage
    class Meta:
        verbose_name_plural = "status"
        
class Support(models.Model):
    team = models.CharField(max_length=200)
    def __str__(self):
        return self.team
    class Meta:
        ordering = ['team']
        verbose_name_plural = "support"
 
class Location(models.Model):
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.location
    class Meta:
         ordering = ['location']

class Availability(models.Model):
    hours = models.CharField(max_length=200)
    def __str__(self):
        return self.hours
    class Meta:
        ordering = ['hours']
        verbose_name_plural = "availability"

class Service(models.Model):
    name = models.CharField(max_length=200)
    guid = models.UUIDField(primary_key=False, default=None, null=True, blank=True, editable=True)
    summary = models.CharField(max_length=140, default=None, blank=True, null=True)
    description = models.TextField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default=None, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True, null=True)
    type = models.ManyToManyField(Type)
    required_by = models.ManyToManyField('self', blank=True)
    requires = models.ManyToManyField('self', blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=None, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    business_owner = models.ForeignKey(People, related_name='bo', on_delete=models.CASCADE, default=None, blank=True, null=True)
    service_owner = models.ForeignKey(People, related_name='so', on_delete=models.CASCADE, default=None, blank=True, null=True)
    service_operations_manager = models.ManyToManyField(People, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None, blank=True, null=True)
    support = models.ForeignKey(Support, on_delete=models.CASCADE, default=None, blank=True, null=True)
    second_line_support = models.ForeignKey(Support,related_name='second_line_support', on_delete=models.CASCADE, default=None, blank=True, null=True)
    documentation = models.CharField(max_length=200,  blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE, blank=True, null=True)
    logo = models.ImageField(upload_to=only_filename, default=None, blank=True, null=True)
    published = models.BooleanField(default=0)
    
    
    def __str__(self):
        return self.name
 
    class Meta:
         ordering = ['name']


        
    

