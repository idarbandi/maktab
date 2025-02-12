# profiles/views.py
from django.db.models import Count, Q

# profiles/views.py
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment, Notification, Post, User, UserProfile
from .serializers import (
    CommentSerializer,
    NotificationSerializer,
    PostSerializer,
    UserProfileSerializer,
    UserSerializer,
)


class SearchView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query))
        users = User.objects.filter(
            Q(username__icontains=query) | Q(email__icontains=query))
        return {'posts': PostSerializer(posts, many=True)
                .data, 'users': UserSerializer(users, many=True).data}

    def list(self, request, *args, **kwargs):
        response = self.get_queryset()
        return Response(response)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        post_id = self.request.query_params.get('post', None)
        if post_id is not None:
            return Comment.objects.filter(post_id=post_id)
        return super().get_queryset()

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = self.get_object()
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        return Response({'status': 'like toggled', 'like_count': comment.like_count})


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


class UserProfileUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        user_profile = request.user.userprofile
        serializer = UserProfileSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


# Check USers Authority


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


# profiles/filters & sort


class FilterSortPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        tag = self.request.query_params.get('tag')
        sort_by = self.request.query_params.get('sort_by')

        if category:
            queryset = queryset.filter(categories__name=category)
        if tag:
            queryset = queryset.filter(tags__name=tag)
        if sort_by == 'popularity':
            queryset = queryset.annotate(
                like_count=Count('likes')).order_by('-like_count')
        elif sort_by == 'date':
            queryset = queryset.order_by('-created_at')

        return queryset


class UserDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        user_data = UserSerializer(user).data
        # Assuming user has a related name 'posts'
        recent_posts = user.posts.order_by('-created_at')[:5]
        # Assuming user has a related name 'notifications'
        notifications = user.notifications.order_by('-created_at')[:5]

        data = {
            'user': user_data,
            'recent_posts': PostSerializer(recent_posts, many=True).data,
            'notifications': NotificationSerializer
            (notifications, many=True).data
        }
        return Response(data)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)


# profiles/views.py


class IDAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            # Admin-specific logic here
            return Response({"message": "You are an admin"})
        else:
            return Response({"message": "You are not an admin"}, status=403)
