#django
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
posts = [

    {
        
        'title': 'Mont Blanc',
        'user': {
            'name': 'Mont Blantesco Pradez Biso',
            'picture': 'https://picsum.photos/id/223/60/60'
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/234/200/200'                                   
    },
    {
        
        'title': 'Perez Loco',
        'user': {
            'name': 'Perito Perez Delirio',
            'picture': 'https://picsum.photos/id/244/60/60'
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/233/200/200'                                   
    },
    {
        
        'title': 'Rumualdo Fons',
        'user': {
            'name': 'Rumualdo Bildefonso Fonso',
            'picture': 'https://picsum.photos/id/243/60/60'
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/232/200/200'                                   
    },
    {
        
        'title': 'Regina Andares',
        'user': {
            'name': 'Regina Andares Cifuentes',
            'picture': 'https://picsum.photos/id/242/60/60'
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/231/200/200'                                   
    },
    {
        
        'title': 'Benito Caméla',
        'user': {
            'name': 'Benito Lopez Peroto Caméla',
            'picture': 'https://picsum.photos/id/241/60/60'
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/230/200/200'                                   
    },
    
]
@login_required
def list_posts(request):
  return render(request, 'posts/feed.html', {'posts': posts})
# Create your views here.
