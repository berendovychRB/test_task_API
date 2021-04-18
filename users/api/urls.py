from django.urls import path

from .views import GroupAPIView, UserAPIView, UserDetailApiView, GroupDetailApiView

urlpatterns = [
    path('groups/', GroupAPIView.as_view(), name='groups'),
    path('users/', UserAPIView.as_view(), name='users'),
    path('users/<int:pk>', UserDetailApiView.as_view(), name='user_detail'),
    path('groups/<int:pk>', GroupDetailApiView.as_view(), name='group_detail'),
]