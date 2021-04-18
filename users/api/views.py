from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import GroupSerializer, UserSerializer
from ..models import Group, User


class GroupAPIView(ListCreateAPIView):

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupDetailApiView(RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAPIView(ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailApiView(RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


