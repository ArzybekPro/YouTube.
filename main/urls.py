
from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
from django.views.generic import TemplateView


api_urlpatterns =[
    path('users/',include('apps.users.urls')),
    path('settings/',include('apps.settings.urls')),
    path('videos/',include('apps.videos.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(api_urlpatterns)),
    

    path('/',TemplateView.as_view(template_name = 'index.html')),
    path('',TemplateView.as_view(template_name = 'index.html')),
    path('user/user',TemplateView.as_view(template_name = 'index.html')),
    path('user/login',TemplateView.as_view(template_name = 'index.html')),
    path('user/register',TemplateView.as_view(template_name = 'index.html')),
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
