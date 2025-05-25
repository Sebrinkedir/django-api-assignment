from rest_framework import serializers
from .models import Post  # Make sure Post is correctly defined in models.py

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
