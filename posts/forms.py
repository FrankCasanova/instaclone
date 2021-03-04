


from django import forms
from django.forms import fields

#model
from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ('user', 'profile', 'title', 'photo', )

