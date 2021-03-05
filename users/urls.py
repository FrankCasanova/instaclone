
from django.urls import path
 
from users import views

urlpatterns = [



    #management
    path(
        route='login/',
        view=views.LoginView.as_view(), 
        name='login'),
    path(
        route='logout/',
        view=views.LogOutView.as_view(), 
        name='logout'),
    path(
        route='signup/',
        view=views.SignUpView.as_view(),
        name='signup'),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(), 
        name='update'),
    #post
    path(
        route='<str:username>',
        view= views.UserDetailView.as_view(),
        name='detail'
    ),
]
