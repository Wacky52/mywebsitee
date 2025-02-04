from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=100)
    subject_tutor = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    price = models.CharField(max_length=100)
    details = models.TextField()
    slug = models.SlugField(null=False,unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title