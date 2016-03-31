from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf


def home(request):
    return render(request, 'market/home.html', {})


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('market/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response(
        'market/loggedin.html',
        {'username': request.user.username}
    )


def invalid_login(request):
    return render_to_response('market/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('market/logout.html')
