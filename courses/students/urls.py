from django.conf.urls import url
from .views import students_list, student_item

urlpatterns = [
    url(r'^students/$', students_list),
    url(r'^students/(?P<student_id>\d+)/$', student_item),
]
