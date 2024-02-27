from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView
import re
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
 
class HomePageView(TemplateView):
    template_name = 'home.html'

@csrf_exempt
def calculate_sum(request):
    if request.method == 'POST':
        value1 = request.POST.get('value1', 0)
        value2 = request.POST.get('value2', 0)
        # vv = check(value1)
        result = sum(value1, value2)
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Метод не поддерживается'}, status=405)

def sum(value1, value2):
    return float(value1) + float(value2)

def plot_graph(request):
    x = np.arange(0, 10, 1)
    y = 2 * x

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График y=2*x')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return HttpResponse(buffer, content_type='image/png')
