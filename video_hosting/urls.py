from django.urls import path
from .video_views import VideoView
from .comment_views import CommentView
from .hash_tag_views import HashTagRetrieveUpdateDeleteView, HashTagListCreateView

# videos
urlpatterns = [
    path("videos/create/", VideoView.as_view()),
    path("videos/get/<int:pk>/", VideoView.as_view()),
    path("videos/get/", VideoView.as_view()),
    path("videos/update/<int:pk>/", VideoView.as_view()),
    path("videos/delete/<int:pk>/", VideoView.as_view())
]

# comments
urlpatterns += [
    path("comment/create/", CommentView.as_view()),
    path("comment/get/<int:pk>/", CommentView.as_view()),
    path("comment/get/", CommentView.as_view()),
    path("comment/update/<int:pk>/", CommentView.as_view()),
    path("comment/delete/<int:pk>/", CommentView.as_view())
]

# hash tag
urlpatterns += [
    path("hashtag/", HashTagListCreateView.as_view()),
    path("hashtag/<int:pk>/", HashTagRetrieveUpdateDeleteView.as_view())
]