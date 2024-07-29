from django.shortcuts import render
from rest_framework import generics
from .models import Category, Topic
from .serializers import CategorySerializer, TopicSerializer

class TopicView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

def getRandomTopicAPI(request):
    all_topics = Topic.objects.all()
    scrape()
    

