from django.http import HttpRequest
from django.http import JsonResponse

def api_home(_: HttpRequest):
    return JsonResponse({
        'status': 'UP'
    })
