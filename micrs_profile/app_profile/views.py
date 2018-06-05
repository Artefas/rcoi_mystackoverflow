from django.shortcuts import render


from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.

from rest_framework import generics

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

