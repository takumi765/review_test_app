from django.shortcuts import render
from .models import Test

def index(request):
  if request.method == 'GET':
    tests_list = {}
    tests = Test.objects.all()
    tests_list["tests_list"] = tests
    return render(request, 'index.html', tests_list)
  elif request.method == 'POST':
    return render(request, 'index.html')
