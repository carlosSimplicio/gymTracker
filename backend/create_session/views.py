from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def create_session(request):
    session_data = request.POST.dict()
    print(session_data)
    return HttpResponse('received', status=201)
