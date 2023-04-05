from django.contrib import admin
from .models import Package,Itinerary
# Register your models here.

class ToursPackage(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('name',)
    }

    list_display  = ('name','slug')
admin.site.register(Package,ToursPackage)
admin.site.register(Itinerary)




