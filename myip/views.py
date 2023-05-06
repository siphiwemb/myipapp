from django.http import JsonResponse

def custom_404(request, exception):
    data = {'error': 'The requested resource was not found.'}
    return JsonResponse(data, status=404)

def custom_500(request):
    data = {'error': 'Internal server error.'}
    return JsonResponse(data, status=500)