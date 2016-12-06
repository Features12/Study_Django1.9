from django.conf.urls import url
from .views import output, garbage, items_details, logins, reg, logout_view,shop_cart, buy_items, news_page

urlpatterns = [
    url(r'^$', news_page),#main page
    url(r'^garbage/$', garbage), #garbage
    url(r'^garbage/(?P<id>\w)$', shop_cart), #details cart shop
    url(r'^garbage/buy_all/$', buy_items),
    url(r'^items_details/(?P<id>\w)$', items_details), # more details page
    url(r'^login/$', logins), # login users
    url(r'^logout/$', logout_view), # logout users
    url(r'^reg/$', reg), # registration users
    url(r'^shop/$', output) # shop page
    ]