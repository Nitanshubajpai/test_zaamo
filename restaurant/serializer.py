from django.db.models.fields import Field
from .models import restaurant
from rest_framework import serializers

class restaurantserializer(serializers.BaseSerializer):
    class meta:
        fields = '__all__'
        model = restaurant