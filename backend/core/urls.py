from django.urls import path
from core import views

urlpatterns = [
    path("session", views.create_session),
    path("exercise/list", views.list_exercises),
    path("session/list", views.list_sessions),
    path("auth/login", views.sign_in),
    path("auth/logout", views.sign_out),
    path("auth/whoami", views.who_am_i)
]
