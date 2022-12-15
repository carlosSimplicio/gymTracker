from core import service
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@require_POST
@login_required
def create_session(request):
    session_data = request.POST.dict()
    created_session = service.create_service(session_data)
    return JsonResponse(created_session, status=201)

@require_GET
@login_required
def list_exercises(_):
    exercises = service.list_exercises()
    return JsonResponse(exercises, safe=False)

@require_GET
@login_required
def list_sessions(_):
    sessions = service.list_sessions()
    return JsonResponse(sessions, safe=False)

@ensure_csrf_cookie
@require_POST
def sign_in(request):
    form = request.POST.dict()
    user = authenticate(username=form['username'], password=form['password'])
    if user:
        login(request, user)
        return HttpResponse(status=200)

    return HttpResponse(status=401)

@login_required
def who_am_i(request):
    if request.user.is_authenticated:
        user = request.user
        return JsonResponse({
            'authenticated': True,
            'id': user.id,
            'name': user.first_name + ' ' + user.last_name,
            'email': user.email
        })

    return JsonResponse({'authenticated': False})
