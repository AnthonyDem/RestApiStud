from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment, Video
from .serializers import CommentSerializer


class CommentView(APIView):

    def post(self, request):
        video_id = request.data.get("video")
        content = request.data.get("content")
        video = Video.objects.get(id=video_id)
        comment = Comment.objects.create(video=video, content=content)
        comment_serialized = CommentSerializer(comment).data
        return Response(comment_serialized)

    def get(self, request, pk=None):
        try:
            if not pk:
                comments = Comment.objects.all()
                comments_serialized = CommentSerializer(comments, many=True).data
                return Response(comments_serialized)
            comment = Comment.objects.get(id=pk)
            comment_serialized = CommentSerializer(comment).data
            return Response(comment_serialized)
        except ObjectDoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
