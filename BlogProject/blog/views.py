from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class PostList(APIView):
    @swagger_auto_schema(responses={200: PostSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        module1_objects = Post.objects.all()
        serializer = PostSerializer(module1_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: PostSerializer(many=True)})
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get(self, request, module1_id, *args, **kwargs):
        module1_object = get_object_or_404(Post, id=module1_id)
        serializer = PostSerializer(module1_object)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, module1_id, *args, **kwargs):
        module1_object = get_object_or_404(Post, id=module1_id)
        serializer = PostSerializer(module1_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, module1_id, *args, **kwargs):
        module1_object = get_object_or_404(Post, id=module1_id)
        module1_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    @swagger_auto_schema(responses={200: CommentSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        module2_objects = Comment.objects.all()
        serializer = CommentSerializer(module2_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: CommentSerializer(many=True)})
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    def get(self, request, module1_id, *args, **kwargs):
        module1_object = get_object_or_404(Comment, id=module1_id)
        serializer = CommentSerializer(module1_object)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, module1_id, *args, **kwargs):
        module1_object = get_object_or_404(Comment, id=module1_id)
        serializer = CommentSerializer(module1_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, module1_id, *args, **kwargs):
        module1_object = get_object_or_404(Comment, id=module1_id)
        module1_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)