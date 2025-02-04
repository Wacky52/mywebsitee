from django.db import models

# Create your models here.


class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=100)
    smtp_email = models.EmailField()
    smtp_password = models.CharField(max_length=100)
    smtp_port = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    icon =  models.ImageField(upload_to='images/')
    aboutus = models.TextField(max_length=255)
    contact = models.CharField(max_length=100)

