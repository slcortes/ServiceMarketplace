from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from market.forms import MyRegistrationForm
from market.models import Service


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
    args = {}
    if request.method == "POST":  # Occurs after user submits info
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')
        else:
            args['errors'] = form.errors

    args.update(csrf(request))

    args['form'] = MyRegistrationForm()
    return render_to_response('market/register.html', args)


def register_success(request):
    return render_to_response('market/register_success.html')


# Search view
def search(request):
    query = request.GET.get('q')
    if query:
        # user entered query
        results = (Service.objects.filter(title__contains=query) |        \
                   Service.objects.filter(description__contains=query)).order_by('-created_date')
    else:
        # user did not enter query. return all results
        results = Service.objects.all().order_by('-created_date')
    return render(request, 'market/search_result.html', {'results': results})

