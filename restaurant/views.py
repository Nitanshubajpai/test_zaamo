from django.http import response
from django.shortcuts import render
from rest_framework.fields import CurrentUserDefault
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
                currect_object = {}
                currect_object["name"]=i.name
                currect_object["type"]=i.type
                currect_object["description"]=i.description
                response.append(currect_object)
            return JsonResponse({"data":response})
        except Exception as e:
            return JsonResponse({"data":e})
                
