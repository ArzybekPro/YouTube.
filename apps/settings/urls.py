from django.urls import path
from .views import SettingsAPIView,SettingsCreateAPIView,SettingsUpsateAPIView
urlpatterns = [
    path('',SettingsAPIView.as_view()),
    path('create/',SettingsCreateAPIView.as_view()),
    path('update/<int:pk>/',SettingsUpsateAPIView.as_view()),
]
