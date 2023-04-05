from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    author = models.CharField(max_length=100)

    def get_url(self):
      return reverse('blog_details',args={self.slug
                                            })

    def __str__(self):
        return self.title