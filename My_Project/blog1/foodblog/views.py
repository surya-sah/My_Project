from django.shortcuts import render
from rest_framework.response import Response
from . models import Post
from . serializers import PostSerializer
from rest_framework.views import APIView

# Create your views here.
class ListPostAPIView(APIView):
    def get(self,request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

class PostdetailAPIView(APIView):
    def get(self,request,pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)

class CreatePostAPIView(APIView):
    def post(self,request):
        #print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdatePostAPIView(APIView):
    def post(self,request,pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeletePostAPIView(APIView):
    def get(self,request,pk):
        post = post.objects.get(id=pk)
        post_instance = post.objects.get(id=pk)
        post_instance.delete()
        return Response('Deleted')

