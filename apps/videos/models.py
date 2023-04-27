from django.db import models
from apps.users.models import User
from django.utils.text import slugify

class Video(models.Model):
    
    title = models.CharField(
        max_length=50
    )
    
    description  = models.CharField(
        max_length=100
    )
    poster = models.FileField(
        upload_to = 'poster/'
    )
    video_file = models.FileField(
        upload_to = 'video_file/'
    )
    channel = models.ForeignKey(
        User,
        related_name = 'user_video',
        on_delete = models.CASCADE
    )

    slug = models.SlugField(
        max_length=255,
        unique = True,
        auto_created=True
        
    )
    
    
    created = models.DateTimeField(
        auto_now_add=True
    )
    def save(self , *args ,**kwars):
        self.slug = slugify(self.title)
        super(Video,self).save(*args, **kwargs)
        
        
        
class VideoLike(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='user_like',
        on_delete=models.CASCADE
    )
    to_video = models.ForeignKey(
        Video,
        related_name='video_like',
        on_delete=models.CASCADE
    )

class VideoDisLike(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='user_dislike',
        on_delete=models.CASCADE
    )
    to_video = models.ForeignKey(
        Video,
        related_name='video_dislike',
        on_delete=models.CASCADE
    )

class VideoViews(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='user_views',
        on_delete=models.CASCADE
    )
    to_video = models.ForeignKey(
        Video,
        related_name='video_views',
        on_delete=models.CASCADE
    )