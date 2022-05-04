from rest_framework import generics

from video_hosting.models import HashTag
from video_hosting.serializers import HashTagSerializer


class HashTagListCreateView(generics.ListCreateAPIView):
    serializer_class = HashTagSerializer
    queryset = HashTag.objects.all()


class HashTagRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HashTagSerializer
    queryset = HashTag.objects.all()