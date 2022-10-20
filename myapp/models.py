from distutils.command.upload import upload
import email
from django.db import models

# Create your models here.

class Contact(models.Model):
    email=models.EmailField()
    address=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    product_description=models.TextField()
    img=models.ImageField(upload_to='pics')

class Image(models.Model):

    banner_img=models.FileField(upload_to='pics')
    about_banner_img=models.FileField(upload_to='pics')
    logo_img=models.ImageField(upload_to='pics')
    
class Socialmedia(models.Model):
    facebook = models.URLField(max_length = 200)
    linkedin = models.URLField(max_length = 200)
    whatsapp = models.URLField(max_length = 200)
    
class Text(models.Model):
    about_us=models.TextField()
    banner_heading=models.CharField(max_length=100)
    banner_text=models.TextField()

class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    



