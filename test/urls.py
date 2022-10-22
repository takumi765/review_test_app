from django.urls import path
from . import views

app_name='test'

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_account, name='logout'),
    path('create_user', views.create_user, name='create_user'),
    path("create/", views.create, name="create"),
    path("exam/", views.exam, name="exam"),
    path("history/", views.history, name="history"),
    path("update/", views.update, name="update"),
]