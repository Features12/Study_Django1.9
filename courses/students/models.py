from django.db import models

class Student(models.Model):

    package_choice = (
        ("standart","Standart"),
        ("gold", "Gold"),
        ("vip", "Vip"),
    )

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=15, choices= package_choice)
    note = models.TextField(blank=True)


