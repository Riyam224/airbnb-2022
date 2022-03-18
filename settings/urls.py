from django.urls import path
from .views import home , home_search , category_filter , contact_us , news_letter_subscribe  , dashboard



app_name = 'settings'

urlpatterns = [
    path('',  home , name='home'),
    path('search/' , home_search , name="home_search"),

    # todo dashboard 
    path('dashboard/', dashboard , name='dashboard'),
    # todo contact us 


    path('contact_us/', contact_us, name='contact_us'),
    path('newsletter/' , news_letter_subscribe , name='newsletter'),
    path('categoty/<slug:category>/' ,  category_filter , name='category_filter'),
]