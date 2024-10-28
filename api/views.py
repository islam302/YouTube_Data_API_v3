import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

API_KEY = 'AIzaSyCDtuiyRmWnIrT7uJu_A0RvrUdOON3yqLE'


def extract_video_id(url):
    # if url short :
    if 'youtu.be' in url:
        return url.split('/')[-1]
    # if url tall:
    elif 'youtube.com' in url:
        return url.split('v=')[-1].split('&')[0]
    return None


def get_youtube_video_info(video_id):
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=snippet&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if 'items' in data and len(data['items']) > 0:
        snippet = data['items'][0]['snippet']
        return {
            'title': snippet['title'],
            'thumbnail': snippet['thumbnails']['high']['url'],
            'description': snippet['description'],
            'url': f'https://youtu.be/{video_id}'
        }
    else:
        return None


@csrf_exempt
def get_video_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        video_url = data.get('url')
        video_id = extract_video_id(video_url)
        info = get_youtube_video_info(video_id)
        if info:
            return JsonResponse(info)
        else:
            return JsonResponse({"error": "Video not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
