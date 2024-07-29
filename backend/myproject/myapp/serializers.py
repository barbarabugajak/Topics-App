from .models import Category, Topic
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class TopicSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Topic
        fields = ['id', 'name', 'link', 'category', 'language']