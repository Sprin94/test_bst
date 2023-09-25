import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from robots.forms import RobotForm


@csrf_exempt
def create_robot(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method not allowed'}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'invalid json'}, status=400)

    form = RobotForm(data)
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)
    form.save()
    response_data = {"detail": "Robot added."}
    return JsonResponse(response_data, status=201)
