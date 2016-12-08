from django.conf.urls import url
from .views import shop_output_list, garbage, items_details, logins, reg, logout_view,shop_cart, buy_items, news_page, news_details

urlpatterns = [
    url(r'^$', news_page),#main page
    url(r'^(?P<id>\w{1,2})$',news_details), # details news page
    url(r'^garbage/$', garbage), #garbage
    url(r'^garbage/(?P<id>\w{1,2})$', shop_cart), #details cart shop
    url(r'^garbage/buy_all/$', buy_items),
    url(r'^items_details/(?P<id>\w{1,2})$', items_details), # more details page
    url(r'^login/$', logins), # login users
    url(r'^logout/$', logout_view), # logout users
    url(r'^reg/$', reg), # registration users
    url(r'^shop/$', shop_output_list) # shop page
    ]