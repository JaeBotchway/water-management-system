from django.shortcuts import render
from rest_framework import generics 
from rest_framework.generics import CreateAPIView
from .serializer import UserSerializer

# Create your views here.
class CreateAccount(generics.CreateAPIView):
    serializer_class=UserSerializer