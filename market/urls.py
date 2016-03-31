from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # Service
    url(r'^service/create/$', views.service_create, name="service_create"),

    # Auth URLs
    url(r'^accounts/login/$', views.login),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid/$', views.invalid_login),
    url(r'^accounts/register/$', views.register_user),
    url(r'^accounts/register_success/$', views.register_success),

    # Search
    url(r'^search/$', views.search, name="search"),
]
