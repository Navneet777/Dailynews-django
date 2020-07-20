from django.contrib.sitemaps  import Sitemap
from django.urls import reverse
from crypto.models import Post
class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index','home' , 'que' , 'news', 'about',
        'india','indiasport','indiascience','indiaBussiness','indiaEntertainment',
        'usa','usasport','usascience','usaBussiness','usaEntertainment',
        'china','chinasport','chinascience','chinaBussiness','chinaEntertainment',
        'russia','russiasport','russiascience','russiaBussiness','russiaEntertainment','loginuser','Contactus','subscribe']

    def location(self, item):
        return reverse(item)
