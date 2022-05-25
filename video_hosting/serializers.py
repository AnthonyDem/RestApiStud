from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import Video, Comment, HashTag, VideoRecommendation, Channel
from .models import User


class UserCreateCustomSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'likes_count', 'user', 'comments', 'title', 'link')
        model = Video


class VideoFullSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ('__all__')
        exclude = ('link',)
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


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "subscribers", "owner")
        model = Channel


class UserSubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("id", "email", "subscriptions")
        model = User