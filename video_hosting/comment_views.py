from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from openpyxl import Workbook
from openpyxl.styles import Alignment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment, Video, User
from .serializers import CommentSerializer
from rest_api_video.celery import clear_comments


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

    @method_decorator(cache_page(60 * 2))
    @method_decorator(vary_on_headers("Authorization", ))
    def get(self, request, pk=None):
        try:
            if not pk:
                comments = Comment.objects.all()
                comments_serialized = CommentSerializer(comments, many=True).data
                clear_comments.delay()
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


class ExportMyCommentsView(APIView):

    def get(self, request):
        # current_user = request.user
        # my_comments = Comment.objects.filter(owner_id=current_user.id)
        my_comments = Comment.objects.all()
        alignment = Alignment(horizontal='center', vertical='center', )
        workbook = Workbook()
        ws = workbook.active
        fields = ['Owner', 'Video', 'Content', 'Likes count']
        column = 1
        row = 1
        for field in fields:
            cell = ws.cell(column=column, row=1, value=field)
            cell.alignment = alignment
            column += 1
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename=Data.xlsx'
        workbook.save(response)
        return response
