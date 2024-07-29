from django.shortcuts import render
from rest_framework import generics
from .models import Category, Topic
from .serializers import CategorySerializer, TopicSerializer
from .scraper import scrape
import random

class TopicView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

def getRandomTopicAPI(request):
    scrape()
    all_topics = Topic.objects.all()
    random_topic = random.choice(all_topics)
    serializer = TopicSerializer(random_topic)
    return Response(serializer.data)


