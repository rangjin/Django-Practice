from django.shortcuts import redirect
from user.models import User


def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = User.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrap
