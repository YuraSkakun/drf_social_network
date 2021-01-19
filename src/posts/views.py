from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, UserLike
from posts.serializers import PostSerializer, UserLikeSerializer, PostBriefSerializer
from posts.permissions import IsOwner


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self):
        obj = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return obj


class UserLikeList(generics.ListCreateAPIView):
    queryset = UserLike.objects.all()
    serializer_class = UserLikeSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)


class UserLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserLikeSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self):
        obj = get_object_or_404(UserLike, pk=self.kwargs.get('user_like_id'))  # , user=self.request.user)
        return obj
