from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CompanySerializer
from .serializers import LocationSerializer
from .models import companies
from .models import locations

# POST/GET Company/Location
class companiesList(generics.ListCreateAPIView):
    queryset = companies.objects.all().order_by('id')
    serializer_class = CompanySerializer

class companiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = companies.objects.all().order_by('id')
    serializer_class = CompanySerializer

class locationsList(generics.ListCreateAPIView):
    queryset = locations.objects.all().order_by('id')
    serializer_class = LocationSerializer

class locationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = locations.objects.all().order_by('id')
    serializer_class = LocationSerializer