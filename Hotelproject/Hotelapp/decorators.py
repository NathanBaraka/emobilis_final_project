from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponse("You are not allowed to access this page")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            group_names = [group.name for group in request.user.groups.all()]
            if 'admin' in group_names:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to view this list")
        else:
            return redirect('login')  # Redirect unauthenticated users to login
    return wrapper_func