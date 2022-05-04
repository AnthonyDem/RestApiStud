from django.urls import path
from .video_views import VideoView
from .comment_views import CommentView

# videos
urlpatterns = [
    path("videos/create/", VideoView.as_view()),
    path("videos/get/<int:pk>/", VideoView.as_view()),
    path("videos/get/", VideoView.as_view())
]

# comments
urlpatterns += [
    path("comment/create/", CommentView.as_view()),
    path("comment/get/<int:pk>/", CommentView.as_view()),
    path("comment/get/", CommentView.as_view())
]