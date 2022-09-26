from django.http import JsonResponse


def hello(_):
    return JsonResponse("Hello", safe=False)
