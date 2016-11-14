from django.conf.urls import url
from .views import output, garbage, items_details, login, reg

urlpatterns = [
    url(r'^', output),#main page
    url(r'^garbage/$', garbage), #garbage
    url(r'^items_details/$', items_details), #info items
    url(r'^login/$', login), # login
    url(r'^reg/$', reg), # registration
    ]