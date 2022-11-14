from django.urls import path

from . import views

app_name = 'rest_api'

urlpatterns = [
    path('test/', views.test_list, name='test'),
]