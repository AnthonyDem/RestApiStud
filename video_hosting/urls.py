from django.urls import path

from .user_views import ListUsersView, ResetPasswordView, ChannelSubscribeView, ChannelView
from .video_views import VideoView, OnlyMyVideoView
from .comment_views import CommentView, ExportMyCommentsView
from .hash_tag_views import HashTagRetrieveUpdateDeleteView, HashTagListCreateView

# videos
urlpatterns = [
    path("videos/create/", VideoView.as_view()),
    path("videos/get/<int:pk>/", VideoView.as_view()),
    path("videos/get/", VideoView.as_view()),
    path("videos/get-my/", OnlyMyVideoView.as_view()),
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

urlpatterns += [
    path("password/reset_password/", ResetPasswordView.as_view())
]

# urlpatterns += [
#     path("users/", ListUsersView.as_view())
# ]

urlpatterns += [
    path("channel/", ChannelView.as_view()),
    path("channel/all-my/", ChannelView.as_view())
]

urlpatterns += [
    path("subscribe/", ChannelSubscribeView.as_view()),
    path("channel/subscriptions/<int:pk>/", ChannelSubscribeView.as_view()),
    path("unsubscribe/<int:pk>/", ChannelSubscribeView.as_view())
]

urlpatterns += [
    path("export/comments/", ExportMyCommentsView.as_view())
]