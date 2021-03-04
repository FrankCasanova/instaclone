#django
from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView
from django.urls import reverse

#form
from posts.forms import PostForm

#utilities
from datetime import datetime

#models
from posts.models import Post

# posts = [

#     {
        
#         'title': 'Mont Blanc',
#         'user': {
#             'name': 'Mont Blantesco Pradez Biso',
#             'picture': 'https://picsum.photos/id/223/60/60'
#         },
#         'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/id/234/200/200'                                   
#     },
#     {
        
#         'title': 'Perez Loco',
#         'user': {
#             'name': 'Perito Perez Delirio',
#             'picture': 'https://picsum.photos/id/244/60/60'
#         },
#         'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/id/233/200/200'                                   
#     },
#     {
        
#         'title': 'Rumualdo Fons',
#         'user': {
#             'name': 'Rumualdo Bildefonso Fonso',
#             'picture': 'https://picsum.photos/id/243/60/60'
#         },
#         'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/id/232/200/200'                                   
#     },
#     {
        
#         'title': 'Regina Andares',
#         'user': {
#             'name': 'Regina Andares Cifuentes',
#             'picture': 'https://picsum.photos/id/242/60/60'
#         },
#         'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/id/231/200/200'                                   
#     },
#     {
        
#         'title': 'Benito Caméla',
#         'user': {
#             'name': 'Benito Lopez Peroto Caméla',
#             'picture': 'https://picsum.photos/id/241/60/60'
#         },
#         'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/id/230/200/200'                                   
#     },
    
# ]
# Create your views here.



class PostFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 15
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context



