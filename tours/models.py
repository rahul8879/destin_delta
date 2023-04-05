from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse



class Package(models.Model):
    name                = models.CharField(max_length=100)
    slug                = models.CharField(max_length=100)
    description         = models.TextField(blank=True)
    shrt_desc           = models.TextField(blank=True)
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    image               = models.ImageField(upload_to='tours/photos',blank=True)
    availability        = models.BooleanField(default=True)
    destination         = models.CharField(max_length=100)
    duration            = models.CharField(max_length=100)
    featured            = models.BooleanField(default=False)



    def get_url(self):
      return reverse('package_details',args={self.slug
                                            })

    def __str__(self):
        return self.name


class Itinerary(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='itineraries')
    day = models.PositiveIntegerField()
    description = models.TextField(blank=True)



