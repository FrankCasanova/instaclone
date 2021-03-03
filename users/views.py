
#django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#model
from django.contrib.auth.models import User
from users.models import Profile

#expections
from django.db.utils import IntegrityError

#form
from users.forms import ProfileForm

# Create your views here.


def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')

    else:
        form = ProfileForm()        


    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user':request.user,
            'form': form,
        }

    )







def login_view(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password' })    
       


    return render(request, 'users/login.html')

def logout_view(request):
    logout(request) 
    return redirect('login')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
           return render(request, 'users/signup.html', {'error': 'Password\'s does not match'})
        try:
            user = User.objects.create_user(username=username,password=password)
        except IntegrityError :
            return render(request, 'users/signup.html', {'error': 'The username already in use'})

        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')
          

    return render(request, 'users/signup.html')       


             

