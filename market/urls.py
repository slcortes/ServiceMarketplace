from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # Service
    url(r'^service/create/$', views.service_create, name="service_create"),
    url(r'^service/(?P<pk>\d+)/$', views.service_detail, name="service_detail"),

    # Auth URLs
    url(r'^accounts/login/$', views.login),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid/$', views.invalid_login),
    url(r'^accounts/register/$', views.register_user),
    url(r'^accounts/register_success/$', views.register_success),

    # My Account + Users
    url(r'^my_account/$', views.my_account),
    url(r'^user/(?P<user_id>\d+)/$', views.user_profile, name="user_profile"),
    
    # Review
    url(r'^user/(?P<user_id>\d+)/add_review/$', views.add_review, name="add_review"),
    
    # Search
    url(r'^search/$', views.search, name="search"),
    
    # Browse
    url(r'^browse/$', views.browse, name="browse"),
]




