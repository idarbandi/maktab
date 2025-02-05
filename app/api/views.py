from rest_framework import viewsets

from ..models import Posts
from .serializers import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
