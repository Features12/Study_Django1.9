from django.shortcuts import render
from .models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})


def student_item(request, student_id):
    student = Student.objects.get(id = student_id)
    return render(request, 'item.html', {'student': student})