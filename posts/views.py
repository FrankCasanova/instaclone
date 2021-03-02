#django
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [

    {
        'name': 'Mont Blanc',
        'user': 'troglodita',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/id/237/200/200',
                                        
    },
    {
        'name': 'Pedro Pedrin',
        'user': 'Romulo',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/id/238/200/200',
                                        
    },
    {
        'name': 'Bianca',
        'user': 'Bica',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/id/239/200/200',
                                        
    }
]

def list_posts(request):
    content = []
    [content.append("""

        <p><strong>{name}</strong></p>
        <p><small>{user} -  <i>{timestamp}</i></small></p>
        <figure> <img src="{picture}" alt=""> </figure>

    """.format(**post)) for post in posts]
    return HttpResponse('<br>'.join(content))
# Create your views here.
