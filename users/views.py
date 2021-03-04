
#django
from users.models import Profile
from django.conf.urls import url
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, FormView
from django.views.generic.edit import UpdateView 
from django.urls import reverse
#form
from users.forms import ProfileForm, SingUpForm

#model
from django.contrib.auth.models import User
from posts.models import Post

# Create your views here.

class UserDetailView(LoginRequiredMixin, DetailView):

    
    template_name='users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SingUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return  super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self) -> str:
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username}) 


        


    pass






def login_view(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password' })    
       


    return render(request, 'users/login.html')

def logout_view(request):
    logout(request) 
    return redirect('users:login')



def signup(request):

    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    else:
        form = SingUpForm()

    return render(

        request=request,
        template_name='users/signup.html',
        context={
            'form': form
        }



    )            



             

