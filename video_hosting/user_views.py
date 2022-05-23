from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from video_hosting.models import User
from video_hosting.serializers import UserCreateCustomSerializer


class ListUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateCustomSerializer


class ResetPasswordView(APIView):

    def post(self, request):
        user_id = request.user.id
        password = request.data.get("password")
        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()
        return Response({"message": "password changed successfull!"})