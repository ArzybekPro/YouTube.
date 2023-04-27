from django.urls import path
from apps.users.views import UserAPIView,RegisterAPIView,DestroyAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('',UserAPIView.as_view()),
    path('register/',RegisterAPIView.as_view()),
    path('destroy/<int:pk>/',DestroyAPIView.as_view()),
    
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
