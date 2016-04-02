from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from market.forms import MyRegistrationForm, ServiceForm
from django.contrib.auth.models import User
from market.models import Service, Review




####### Home #######

def home(request):
    return render(request, 'market/home.html', {})




####### Login authorization #######

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




####### Services #######

@login_required
def service_create(request):
    args = {}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.client = request.user
            service.save()
            return HttpResponseRedirect('/browse/')
    else:
        form = ServiceForm()

    args.update(csrf(request))
    args['form'] = form
    return render_to_response('market/service_create.html', args)


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'market/service_detail.html', {'service': service})




####### Reviews #######

"""
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'market/review_detail.html', {'review': review})

def add_review(request, user_id):
    user = get_object_or_404(MainUser, pk=user_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        author = form.cleaned_data['author']
        review = Review()
        review.user = user
        review.author = author
        review.rating = rating
        review.comment = comment
        review.created_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect('/my_account/reviews/')
    return render(request, 'market/profile.html', {'form': form, 'user': user})
"""


####### MyAccount + Users profiles #######

@login_required
def my_account(request):
    reviews = Review.objects.filter(user=request.user).order_by('-created_date')
    return render(request, 'market/my_account.html', {'reviews': reviews})

def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    reviews = Review.objects.filter(user=user).order_by('-created_date')
    return render(request, 'market/user_profile.html', {'user': user, 'reviews': reviews})


        

####### Search view #######

def search(request):
    query = request.GET.get('q')
    if query:
        # user entered query
        results = (Service.objects.filter(title__contains=query) |  \
                   Service.objects.filter(description__contains=query)).order_by('-created_date')
    else:
        # user did not enter query. return all results
        results = Service.objects.all().order_by('-created_date')
    return render(request, 'market/search_result.html', {'results': results})




####### Browse view #######

def browse(request):
    results = Service.objects.all().order_by('-created_date')
    return render(request, 'market/search_result.html', {'results': results})















