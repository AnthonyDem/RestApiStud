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

