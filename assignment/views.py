from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response  
from .models import Country
from .serializers import CountryList  
# Create your views here.

@api_view()
def say_hi(request):
    listing=CountryList(Country)
    return Response(listing.data)
