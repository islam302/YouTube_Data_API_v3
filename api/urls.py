from django.urls import path
from . import views

urlpatterns = [
    path('get_video_info/', views.get_video_info, name='get_video_info'),
]
