from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Topic(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.CharField(max_length=100, choices=(
        ('Polski', 'Polski'),
        ('English', 'English'),
    ))
    
    def __str__(self):
        return self.name