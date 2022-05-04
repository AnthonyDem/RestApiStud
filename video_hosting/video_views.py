from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer


class VideoView(APIView):

    def post(self, request):
        video_data = request.data
        video = Video.objects.create(**video_data)
        serialized_video = VideoSerializer(video).data
        return Response(serialized_video)

    def get(self, request, pk=None):
        if not pk:
            videos = Video.objects.all()
            serialized_video = VideoSerializer(videos, many=True).data
            return Response(serialized_video)
        video = Video.objects.get(id=pk)
        serialized_video = VideoSerializer(video).data
        return Response(serialized_video)
