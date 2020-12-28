
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post

import json

class PostAPI(APIView):

    def post(self, request):

        try:
            data = request.data
            new_post = Post.objects.create(text=data.get('text', None))
            return Response({
                'id': new_post.id,
                'text': new_post.text,
                'created': str(new_post.created),
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        load = []
        posts = Post.objects.all()

        for post in posts:
            load.append({
                'id': post.id,
                'text': post.text,
                'created': str(post.created),
            })

        return Response({'posts': load}, status=status.HTTP_200_OK)
