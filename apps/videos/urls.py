from django.urls import path
from apps.videos.views import VideoAPIView, VieoaCreateAPIView, VieoaDisLikeCreateAPIView, VieoaLikeCreateAPIView, \
    VieoaViewCreateAPIView

urlpatterns = [
    path('', VideoAPIView.as_view()),
    path('create/', VieoaCreateAPIView.as_view()),
    path('view/', VieoaViewCreateAPIView.as_view()),
    path('like/', VieoaLikeCreateAPIView.as_view()),
    path('dislike/', VieoaDisLikeCreateAPIView.as_view()),
]
