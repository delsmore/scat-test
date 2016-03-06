from rest_framework import serializers
from scat.models import Service, People


class ServiceSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Service
        depth = 1
        
class PeopleSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = People
        depth = 1