from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
#class Contact(models.Model):
#    name = models.CharField(max_length = 25)
#    email = models.CharField(max_length = 50)
#    messages = models.CharField(max_length = 200)
class Post(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    slug = models.SlugField(default='',blank=True)

    def save(self, *args , **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('post',args=[str(self.id)])

class Contactmodel(models.Model):
    name = models.CharField(max_length=50, blank=False , null=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    messages = models.CharField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.EmailField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.email

