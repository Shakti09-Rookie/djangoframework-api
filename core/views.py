from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

# original view
# class TestView(APIView):

#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         # serializer = PostSerializer(qs, many=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# def test_view(request):
#     data = {
#         "name" : "Shakti",
#         "age" : 23
#     }
#     return JsonResponse(data)


# secondary view with less code
class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# third view with less code(look in generics.py to see what else we can use)
class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

#fourth with less code than third view and the same functionality
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()