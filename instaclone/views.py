#aqui creamos las vistas
#django
from django.http import HttpResponse, JsonResponse

#utilities
from datetime import datetime




def hello_world(request): #aquí creamos el lugar/vista 

    #con esto indicamos la hora
    now = datetime.now()\
        .strftime('%b %dth, %Y - %H:%M hrs') 

    return HttpResponse(f'hello world! and the time now is {now}')


def sort(request):
    numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])
    return JsonResponse({'lista ordenada':str(numbers)})