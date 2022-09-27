from django.urls import path
from create_session import views

urlpatterns = [path("", views.create_session)]
