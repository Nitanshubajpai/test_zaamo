from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView, Response
from django.http import JsonResponse
from restaurant.models import restaurant
from restaurant.serializer import restaurantserializer
# Create your views here.

class Restaurant(APIView):
    def get(self, request):
        try:
            type = request.GET.get('type')
            objects = restaurant.objects.filter(type=type)
            response = []
            for i in objects:
                current_object = {}
                current_object["name"]=i.name
                current_object["type"]=i.type
                current_object["description"]=i.description
                response.append(current_object)
            return JsonResponse({"data":response})
        except Exception as e:
            return JsonResponse({"data":e})
                
