from django.urls import path
from . import views 
from .api_view import PropertyAPIList , PropertyAPIDetail



app_name = 'property'


urlpatterns = [
    path('' , views.PropertyList.as_view() , name='property_list'),
    path("new/", views.NewProperty.as_view(), name="property_new"),
    path('<slug:slug>/' , views.PropertyDetail.as_view() , name='property_detail'),
    path('category/<str:category>',views.property_by_category , name='property_by_category'),

    # todo api 

    path('api/list/' ,  PropertyAPIList.as_view() , name='property_api_list'),
    path('api/<int:pk>/' ,PropertyAPIDetail.as_view() , name='property_api_detail' ),
]
