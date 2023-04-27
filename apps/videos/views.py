from django.shortcuts import render
from django.forms import model_to_dict
from apps.users.models import User
from rest_framework.response import Response
from rest_framework import generics
from apps.videos.models import Video, VideoViews, VideoLike, VideoDisLike
from apps.videos.serializers import VideoSerializer, VideoLikeSerializer, VideoDisLikeSerializer, VideoViewsSerializer,VideoCreateSerializer



class VideoAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VieoaCreateAPIView(generics.GenericAPIView):
    serializer_class = VideoCreateSerializer
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        title = request.data['title']
        poster = request.data['poster']
        video_file = request.data['video_file']
        description = request.data['description']
        channel = User.objects.get(username = request.data['channel'])
        video = Video.objects.create(
            title = title,
            description=description,
            video_file=video_file,
            poster=poster,
            channel=channel,
        )
        return Response ({'video':model_to_dict(video)})


class VieoaViewCreateAPIView(generics.CreateAPIView):
    queryset = VideoViews.objects.all()
    serializer_class = VideoViewsSerializer


class VieoaLikeCreateAPIView(generics.CreateAPIView):
    queryset = VideoLike.objects.all()
    serializer_class = VideoLikeSerializer


class VieoaDisLikeCreateAPIView(generics.CreateAPIView):
    queryset = VideoDisLike.objects.all()
    serializer_class = VideoDisLikeSerializer


