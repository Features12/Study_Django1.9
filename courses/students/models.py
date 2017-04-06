from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):

    package_choice = (
        ("standart","Standart"),
        ("gold", "Gold"),
        ("vip", "Vip"),
    )

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    slug = models.SlugField() # преобразовывает русский текст
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=15, choices= package_choice)
    note = models.TextField(blank=True)
    group = models.ForeignKey(Group)
    # instance = Student.objects.get(id = 1)
    # instance.group
    # instance.group.name

    def __str__(self):
        return self.name


