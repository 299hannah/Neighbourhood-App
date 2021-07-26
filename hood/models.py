from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.name)


class Neighbourhood(models.Model):
    name=models.CharField(max_length=255)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    created =models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

    @classmethod
    def search_by_title(cls,search_term):
        name = cls.objects.filter(title__icontains=search_term).all()
        return name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = CloudinaryField('image')
    user_name = models.CharField(max_length=255, null=True)
    bio = models.CharField(max_length=255, null=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.TextField()
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    neighbourbood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return self.user_name

    


class Business (models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    neighbourbood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    email =models.EmailField()

    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('business_detail', kwargs={'pk': self.pk})

    

class Post(models.Model):
    content = models.CharField(max_length=255)
    image = CloudinaryField('image',blank=True)
    created = models.DateField(auto_now_add=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255, blank=True )
    
    def delete_post(self):
        self.delete()


    def __str__(self):
        return str(self.content)

  
    def get_absolute_url(self): 
        return reverse('post-detail', kwargs={'pk': self.pk, 'author': self.author})