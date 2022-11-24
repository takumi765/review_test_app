from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json

from test.models import Test
from .serializers import TestSerializer

# Create your views here.
@csrf_exempt
def test_list(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        print(request_data)
        tests = Test.objects.filter(que__icontains=request_data['que'])
        response_data = {'tests': []}
        for test in tests:
            response_data['tests'].append({
                'id': test.id, 
                'subject': test.subject, 
                'que': test.que, 
                'ans': test.ans, 
                'total': test.total, 
                'correct': test.correct, 
                'percent': test.percent, 
                'visibility': test.visibility
            })
        return JsonResponse(data=response_data)
        