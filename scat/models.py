from django.db import models
from django.utils import timezone

class Category(models.Model):
    category = models.CharField(max_length=200)
    summary = models.CharField(max_length=140, default=None, blank=True, null=True)
    image = models.CharField(max_length=100,default=None, blank=True, null=True)
    def __str__(self):
        return self.category
    class Meta:
         ordering = ['category']
		
class Type(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type
		
class Provider(models.Model):
    college = models.CharField(max_length=50)
    school = models.CharField(max_length=150)
    def __str__(self):
        return self.college + ' - ' + self.school
    class Meta:
         ordering = ['college','school']
		
class Person(models.Model):
    uun = models.CharField(max_length=8,default=None, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default=None, blank=True, null=True)
    telephone = models.CharField(max_length=50,default=None, blank=True, null=True)
    department = models.CharField(max_length=100,default=None, blank=True, null=True)
    photo = models.CharField(max_length=100,default=None, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
         ordering = ['name']
		
class Status(models.Model):
    stage = models.CharField(max_length=50)
    def __str__(self):
        return self.stage
        
class Support(models.Model):
    team = models.CharField(max_length=200)
    def __str__(self):
        return self.team
    class Meta:
         ordering = ['team']

class Service(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=140, default=None, blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True, null=True)
    #type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None, blank=True, null=True)
    type = models.ManyToManyField(Type)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=None, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    business_owner = models.ForeignKey(Person, related_name='bo', on_delete=models.CASCADE, default=None, blank=True, null=True)
    service_owner = models.ForeignKey(Person, related_name='so', on_delete=models.CASCADE, default=None, blank=True, null=True)
    service_operations_manager = models.ForeignKey(Person, related_name='som', on_delete=models.CASCADE, default=None, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None, blank=True, null=True)
    support = models.ForeignKey(Support, on_delete=models.CASCADE, default=None, blank=True, null=True)
    documentation = models.CharField(max_length=200, default=None, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
		
    class Meta:
         ordering = ['title']

    def __str__(self):
        return self.title
        
    
		

