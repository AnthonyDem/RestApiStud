from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment, Video, User
from .serializers import CommentSerializer


class CommentView(APIView):

    def post(self, request):
        video_id = request.data.get("video")
        content = request.data.get("content")
        user_id = request.data.get("user_id")
        user = User.objects.get(id=user_id)
        video = Video.objects.get(id=video_id)
        comment = Comment.objects.create(video=video, content=content, user=user)
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

    def put(self, request, pk):
        data = request.data
        Comment.objects.filter(id=pk).update(**data)
        comment_updated = Comment.objects.get(id=pk)
        serialized_video = CommentSerializer(comment_updated).data
        return Response(serialized_video)

    def delete(self, request, pk):
        Comment.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)