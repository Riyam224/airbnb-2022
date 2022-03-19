
from django.shortcuts import redirect, render , get_object_or_404
# Create your views here.
from .models import NewsLetter, Settings
from property.models import Property , Place , Category
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

from settings.models import NewsLetter
from .tasks import send_mail_task

def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()
    restaurant_list = Property.objects.filter(category__name='restaurants')[:4]
    hotels_list =  Property.objects.filter(category__name='hotels')[:4]
    places_list =  Property.objects.filter(category__name='places')[:4]
   
    recent_posts = Post.objects.all()[:4]


    # todo fun facts 

    users_count = User.objects.all().count()
    places_count = Property.objects.filter(category__name='places').count()
    restaurant_count = Property.objects.filter(category__name='restaurants').count()
    hotels_count = Property.objects.filter(category__name='hotels').count()

    context = {
        'places': places,
        'category': category,
        'restaurant_list': restaurant_list,
        'hotels_list': hotels_list,
        'places_list': places_list,

        'recent_posts':recent_posts,


        'users_count': users_count,
        'places_count':places_count,
        'restaurant_count':restaurant_count,
        'hotels_count':hotels_count,
    }
    return render(request , 'settings/home.html', context)



def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property_list = Property.objects.filter(
         
         Q(title__icontains = name) &
         Q(place__name__icontains = place)
    )

    return render(request, 'settings/home_search.html'  , {
        'property_list': property_list
    })




def category_filter(request , category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    return render(request, 'settings/home_search.html'  , {
        'property_list': property_list
    })




def contact_us(request):
   
    site_info = Settings.objects.all()

    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']


        send_mail_task.delay(subject , name,email,message)


    return render(request,'settings/contact.html',{'site_info': site_info})









def news_letter_subscribe(request):
    email = request.POST.get('emailInput')
    NewsLetter.objects.create(email=email)
    return JsonResponse({
        'done': 'done'
    })



def dashboard(request):
     # todo fun facts 

    users_count = User.objects.all().count()
    places_count = Property.objects.filter(category__name='places').count()
    restaurant_count = Property.objects.filter(category__name='restaurants').count()
    hotels_count = Property.objects.filter(category__name='hotels').count()
    context = {
        'users_count':users_count,
        'places_count':places_count,
        'restaurant_count':restaurant_count,
        'hotels_count':hotels_count
    }
    return render(request , 'settings/dashboard.html' , context)