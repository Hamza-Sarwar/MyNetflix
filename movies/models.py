from django.db import models
from categories.models import Category
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title