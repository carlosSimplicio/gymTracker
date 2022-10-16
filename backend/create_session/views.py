from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def set_token(_):
    return HttpResponse(status=200)

def create_session(request):
    print(request.COOKIES)
    session_data = request.POST.dict()
    print(session_data)
    return HttpResponse('received', status=201)
