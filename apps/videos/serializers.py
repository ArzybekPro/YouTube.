from rest_framework import serializers
from apps.videos.models import Video, VideoViews, VideoDisLike, VideoLike
from apps.users.serializers import UserSerializer



class VideoViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoViews
        fields = '__all__'

class VideoDisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDisLike
        fields = '__all__'

class VideoLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLike
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    channel = UserSerializer(many=False)
    video_views = VideoViewsSerializer(many=True,read_only=True)
    video_like = VideoLikeSerializer(many=True, read_only=True)
    video_likes = VideoDisLikeSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = '__all__'


class VideoCreateSerializer(serializers.ModelSerializer):
    channel = serializers.CharField(max_length=255)
    class Meta:
        model = Video
        fields = ('title','description','poster','video_file','channel')