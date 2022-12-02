from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import PostSerializer
from .models import Post



# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET'])
def get_api(request):
    posts = Post.objects.all()
    serailized_posts= PostSerializer(posts, many=True)
    return Response(serailized_posts.data)