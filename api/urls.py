from django.urls import path
from . import views
from .views import extract_emails


urlpatterns = [
    path('test_video_info/', views.get_video_info, name='test_video_info'),  # Change the path
    path('google/', extract_emails, name='extract_emails'),
]
