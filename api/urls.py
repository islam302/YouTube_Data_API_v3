from django.urls import path
from . import views

urlpatterns = [
    path('test_video_info/', views.get_video_info, name='test_video_info'),  # Change the path
]