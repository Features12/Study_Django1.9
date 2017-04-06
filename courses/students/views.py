from django.shortcuts import render, redirect
from .models import Student
from django import forms


class StudentForm(forms.Form):
    CHOICES = (
        ('vip', 'vip'),
        ('standart', 'standart'),
        ('gold', 'gold'),
    )
    student_name = forms.CharField(max_length=100)
    student_package = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    student_note = forms.CharField(widget=forms.Textarea)


def students_list(request):
    students = Student.objects.all()
    page_title = "Students List"
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # process
            return redirect("students_list") # делаем редирект, чтобы нельзя было постить форму с этими данными бесконечное число раз
    else:
        print(request.GET)
        form = StudentForm()
    return render(request, 'list.html', {'students': students,
                                         'title': page_title,
                                         'form':form})


def student_item(request, student_id):
    student = Student.objects.get(id = student_id)
    return render(request, 'item.html', {'student': student})