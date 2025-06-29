from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True) 
    def __str__(self): return self.name
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= 'books')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self): return self.title


# Create your models here.
