#aqui creamos las vistas
#django
from django.http import HttpResponse, JsonResponse

#utilities
from datetime import datetime
import json



def hello_world(request): #aquí creamos el lugar/vista 

    #con esto indicamos la hora
    now = datetime.now()\
        .strftime('%b %dth, %Y - %H:%M hrs') 

    return HttpResponse(f'hello world! and the time now is {now}')


def sort(request):
    numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])
    data = {
        'status': 'ok',
        'numbers':numbers,
        'message':'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request,name,age):
    
    if age < 12:
        message = f'sorry {name} yo\'e not allowed here'
    else:
        message = f'hi {name} welcome'

    return HttpResponse(message)        
