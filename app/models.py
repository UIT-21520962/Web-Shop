from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class Products(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    name = models.CharField(max_length=200, null=False)
    price= models.CharField(max_length=30, null=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=200, default='none')

    def __str__(self):
        return self.name
    
    @property
    def ImageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url
    
class AdvertisingBanner(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title or "Banner"
    
    @property
    def ImageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url
   
    
class Products1(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    name = models.CharField(max_length=200, null=True)
    price= models.CharField(max_length=30, null=False)
    image = models.ImageField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=200, default='none')

    def __str__(self):
        return self.name
    
    @property
    def ImageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url
    
class Products2(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    name = models.CharField(max_length=200, null=True)
    price= models.CharField(max_length=30, null=False)
    image = models.ImageField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=200, default='none')

    def __str__(self):
        return self.name
    
    @property
    def ImageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url



class SocialMediaLink(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url