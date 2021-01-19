from rest_framework import serializers
from .models import Post, UserLike


class UserLikeBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLike
        fields = ('id', 'user', 'active')


class PostBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'date', 'user')


class PostSerializer(serializers.ModelSerializer):

    likes = UserLikeBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'date', 'user', 'likes')


class UserLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLike
        fields = ('id', 'user', 'post', 'active', 'date', 'update')
