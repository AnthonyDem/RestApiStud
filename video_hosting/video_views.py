from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video, User
from .serializers import VideoSerializer, VideoFullSerializer


class VideoView(APIView):

    def post(self, request):
        video_data = request.data
        user_id = request.data.get("user_id")
        user = User.objects.get(id=user_id)
        video = Video.objects.create(user=user, **video_data)
        serialized_video = VideoSerializer(video).data
        return Response(serialized_video)

    def get(self, request, pk=None):
        try:
            if not pk:
                videos = Video.objects.all()
                serialized_video = VideoSerializer(videos, many=True).data
                return Response(serialized_video)
            video = Video.objects.get(id=pk)
            serialized_video = VideoSerializer(video).data
            return Response(serialized_video)
        except ObjectDoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        data = request.data
        Video.objects.filter(id=pk).update(**data)
        video_updated = Video.objects.get(id=pk)
        serialized_video = VideoSerializer(video_updated).data
        return Response(serialized_video)

    def delete(self, request, pk):
        Video.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)


class OnlyMyVideoView(generics.ListAPIView):
    serializer_class = VideoFullSerializer

    def get_queryset(self):
        user = self.request.user
        videos = Video.objects.filter(user=user)
        return videos
