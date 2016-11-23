from django.conf.urls import url
from .views import output, garbage, items_details, logins, reg, logout_view,shop_cart

urlpatterns = [
    url(r'^$', output),#main page
    url(r'^garbage/$', garbage), #garbage
    url(r'^garbage/(?P<id>\w)$', shop_cart),
    url(r'^items_details/$', items_details), #info items
    url(r'^items_details/(?P<id>\w)$', items_details), # more details page
    url(r'^login/$', logins), # login users
    url(r'^logout/$', logout_view), # logout users
    url(r'^reg/$', reg), # registration users
    ]