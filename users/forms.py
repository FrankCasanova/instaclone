#user forms

#django
from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class ProfileForm(forms.Form):

    website = forms.URLField(required=True)
    biography = forms.CharField( max_length=500, required=False)
    phone_number = forms.CharField( max_length=20, required=False)
    picture = forms.ImageField()

class SingUpForm(forms.Form):

    username = forms.CharField(min_length=4,max_length=50, required=True)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())  

    first_name = forms.CharField(min_length=2 ,max_length=50, required=True)
    last_name = forms.CharField(min_length=2 ,max_length=50, required=True)

    email = forms.EmailField(required=True)

    def clean_username(self):
        
        username = self.cleaned_data['username']
        username_query = User.objects.filter(username=username).exists()

        if username_query:
            raise forms.ValidationError('username is already in use')

        return username

    def clean(self):
        '''verify password confirmation match'''
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password_confirmation != password:
            raise forms.ValidationError('passwords do not match.')

        return data


    def save(self):

        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()










