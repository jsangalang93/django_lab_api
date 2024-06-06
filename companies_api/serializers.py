from rest_framework import serializers
from .models import companies, locations

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = companies
        fields = ('name', 'industry',)
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = locations
        fields = ('street', 'city', 'state',)