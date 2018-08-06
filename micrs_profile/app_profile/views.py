from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, ProfileSerializer
from app_profile.models import User, Profile

from rest_framework import generics

class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer