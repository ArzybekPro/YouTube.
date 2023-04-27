from rest_framework import generics 
from apps.settings.models import Settings
from apps.settings.serializers import SettingsSerializers


class SettingsAPIView(generics.ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializers
    
class SettingsCreateAPIView(generics.CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializers
    
class SettingsUpsateAPIView(generics.UpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializers