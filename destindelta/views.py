



from django.shortcuts import render
from tours.models import Package
from blog.models import Blog


from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import os
from twilio.rest import Client
from django.views.decorators.csrf import csrf_protect
from twilio.base.exceptions import TwilioRestException

def home(request):
    popular_pckg  = Package.objects.all().filter(featured=True)
    all_packg     = Package.objects.all().filter(featured=False)
    all_blog      = Blog.objects.all()
    context = {'popular_pckg':popular_pckg,
    'all_packg':all_packg,
    'all_blog':all_blog
    
    }


    return render(request,'home.html',context)

def package_details(request,tour_slug):
    try:
        single_tours = Package.objects.get(slug=tour_slug)
        all_blog      = Blog.objects.all()
        itineraries = single_tours.itineraries.all()
        

    except Exception as e:
        raise e

    context ={'single_tours':single_tours,'itineraries':itineraries,'all_blog':all_blog}

    return render(request,'package_details.html',context)



def blog_details(request, blog_title):
    try:
        single_blog = Blog.objects.get(slug =blog_title )
        all_blog      = Blog.objects.all()
    except Exception as e:
        raise e

    context ={'single_blog':single_blog,'all_blog':all_blog}


    return render(request,'blog.html',context)

def allBlog(request):
    popular_pckg  = Package.objects.all()
    all_blog      = Blog.objects.all()
    context = {'popular_pckg':popular_pckg,
    'all_blog':all_blog,
    }

    return render(request,'blog_archive.html',context)

def packages(request):
    popular_pckg  = Package.objects.all()
    all_blog      = Blog.objects.all()
    context = {'popular_pckg':popular_pckg,
    'all_blog':all_blog,
    }

    return render(request,'all_tours.html',context)



def inquiry(request):

      if request.method == 'POST':
       
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')

        popular_pckg  = Package.objects.all()
      
        all_blog      = Blog.objects.all()
        context = {'popular_pckg':popular_pckg,
        'all_blog':all_blog,
        }

        message_body = "Name: {}\nMobile Number: {}\nCheckin Date: {}\nCheckout Date: {}".format(name, mobile_number, checkin_date, checkout_date)
        print(message_body)
        try:
            print('Inside the try block 1')
                

            account_sid = 'AC8b3c90eabb1fb567b3452895b0d0f2c4'
            auth_token = '49852ee031ffffcd5c94266582c764bc'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_='+16207027359',
            body=message_body,
            to='+919152091676'
            )
        except TwilioRestException as e:
            # Handle exception
            print(e)
            return render(request, 'error.html', {'error': e})
        return render(request, 'success.html')
      return render(request, 'home.html')



def submit_traveler_form(request):
    print('submit_traveler_function called v0.0')
    

    if request.method == 'POST':
        print('Inside the post method v1.0')
        name = request.POST.get('name')
        age = request.POST.get('age')
        num_people = request.POST.get('num_people')
        num_days = request.POST.get('num_days')
        mobile_number = request.POST.get('mobile_number')

        popular_pckg  = Package.objects.all()
        

        all_blog      = Blog.objects.all()
        context = {'popular_pckg':popular_pckg,
        'all_blog':all_blog,
        }

        message_body = "Name:  {}\nNumber of people: {}\nMobile number: {}".format(name, num_people, mobile_number)

        try:
            print('Inside the try block 1')
                

            account_sid = 'AC8b3c90eabb1fb567b3452895b0d0f2c4'
            auth_token = '49852ee031ffffcd5c94266582c764bc'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_='+16207027359',
            body=message_body,
            to='+919152091676'
            )
        except TwilioRestException as e:
            # Handle exception
            print(e)
            return render(request, 'error.html', {'error': e})
        return render(request, 'success.html')
    return render(request, 'home.html')
    
        


    


    