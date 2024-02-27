from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView
import re
 
class HomePageView(TemplateView):
    template_name = 'home.html'

@csrf_exempt
def calculate_sum(request):
    if request.method == 'POST':
        value1 = request.POST.get('value1', 0)
        value2 = request.POST.get('value2', 0)
        vv = check(value1)
        result = sum(value1, value2)
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Метод не поддерживается'}, status=405)

def check(value):
    match = re.match("^(0|[1-9]\d*)([.,]\d+)?", value)
    groups = match.groups()
    if (len(groups)==2):
        return f'{groups[0]}{groups[1]}'
    else:
        return groups[0]

def sum(value1, value2):
    return value1 + value2