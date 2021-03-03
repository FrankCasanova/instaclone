#user forms

#django
from django import forms


class ProfileForm(forms.Form):

    website = forms.URLField(required=True)
    biography = forms.CharField( max_length=500, required=False)
    phone_number = forms.CharField( max_length=20, required=False)
    picture = forms.ImageField()