from rest_framework import serializers
from .models import Video, Comment, HashTag, VideoRecommendation


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'likes_count', 'user', 'comments', 'title', 'link')
        model = Video


class CommentSerializer(serializers.ModelSerializer):
    video = VideoSerializer(many=False)

    class Meta:
        fields = ('id', 'owner', 'video', 'content', 'likes_count')
        model = Comment


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = HashTag


class VideoRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "videos", "recommendation_name", "is_top_rated")
        model = VideoRecommendation
