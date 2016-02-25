from django.db import models
from django.utils import timezone

class Category(models.Model):
    category = models.CharField(max_length=200)
   

   

    def __str__(self):
        return self.category

class Service(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=140, default=None, blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		

