from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),

    # Service
    url(r'^service/create/$', views.service_create, name="service_create"),
    url(r'^service/(?P<pk>\d+)/$', views.service_detail, name="service_detail"),
    url(r'^service/close/(?P<pk>\d+)/$', views.service_close, name="service_close"),
    url(r'^service/update/(?P<pk>\d+)/$', views.service_update, name="service_update"),
    url(r'^bidded/$', views.bidded, name="bidded"),


    # Auth URLs
    url(r'^accounts/login/$', views.login),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/register/$', views.register_user),
    url(r'^accounts/register_success/$', views.register_success),

    # My Account
    url(r'^my_account/$', views.my_account, name="my_account"),

    # User profiles
    url(r'^user/(?P<username>[\w.@+-]+)/$', views.user_profile, name="user_profile"),

    # Review
    url(r'^user/(?P<username>[\w.@+-]+)/add_review/$', views.add_review, name="add_review"),

    # Search
    url(r'^search/$', views.search, name="search"),

    # Browse
    url(r'^browse/$', views.browse, name="browse"),
]
