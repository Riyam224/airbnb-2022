from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListAPIView , ListCreateAPIView ,  RetrieveAPIView , RetrieveUpdateDestroyAPIView



class PropertyAPIList(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer



class PropertyAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
