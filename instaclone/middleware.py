#instaclone middleware

#django
from django.http import response
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompleteMiddleware:

    """
    ensure every users has theirs profiles completes.
    """

    def __init__(self, get_response) -> None:

        self.get_response = get_response


    def __call__(self,request ):

        if not request.user.is_anonymous:
            profile = request.user.profile
            
            if not profile.picture or not profile.biography:
                if not request.user.is_staff:

                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response        