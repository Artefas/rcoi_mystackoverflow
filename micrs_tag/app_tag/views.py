from django.shortcuts import render
from rest_framework import generics

from .models import Tag, QuestionTags
from .serializers import TagSerializer, QuestionTagsSerializer

# Create your views here.

class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class QuestionTagsView(generics.RetrieveAPIView):
    queryset = QuestionTags.objects.all()
    serializer_class = QuestionTagsSerializer

    def get_object(self):


