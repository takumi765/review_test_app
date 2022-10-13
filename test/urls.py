from django.urls import path
from . import views

app_name='test'

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("exam/", views.exam, name="exam"),
    path("history/", views.history, name="history"),
]