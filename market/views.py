from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from market.forms import MyRegistrationForm


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


@login_required()
def loggedin(request):
    return render_to_response(
        'market/loggedin.html',
        {'username': request.user.username}
    )


def invalid_login(request):
    return render_to_response('market/invalid_login.html')


@login_required()
def logout(request):
    auth.logout(request)
    return render_to_response('market/logout.html')


def register_user(request):
    if request.method == "POST":  # Occurs after user submits info
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

    args = {}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()
    return render_to_response('market/register.html', args)


def register_success(request):
    return render_to_response('market/register_success.html')
