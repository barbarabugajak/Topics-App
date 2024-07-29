from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Topic
from .serializers import CategorySerializer, TopicSerializer
from .scraper import scrape
import random

class TopicView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

@api_view(['GET'])
def getRandomTopicAPI(request):
    scrape()
    all_topics = Topic.objects.all()
    print(all_topics)
    random_topic = random.choice(all_topics)
    serializer = TopicSerializer(random_topic)
    return Response(serializer.data)

