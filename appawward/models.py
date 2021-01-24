from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    technology = models.CharField(max_length=300,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    date = models.DateTimeField(auto_now_add=True,blank=True)
    url = models.URLField(max_length=300)
    photo = ImageField(manual_crop='1280x720')
    

    def __str__(self):
        return f"{self.title}"

    def delete_post(self):
        return self.delete

    def save_post(self):
        return self.save()

    @classmethod
    def all_post(cls):
        return cls.objects.all()

    @classmethod
    def get_languages(cls,language):
        language = Post.objects.filter(language=language).all()
        return language

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()
