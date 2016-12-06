from django.contrib.auth.models import User
from django.db import models


class Shop_List(models.Model):
    name = models.CharField(max_length=30) # имя
    kind = models.CharField(max_length=30) # вид
    price = models.FloatField() # цена
    manufacturer = models.CharField(max_length=30) # производитель
    date_receipt = models.DateField() # дата поступления
    type_form = models.TextField(default="1-object") # форма отпуска

    def __str__(self):
        return self.name


class Shop_Cart(models.Model):
    product = models.ForeignKey(Shop_List)
    quantity_product = models.PositiveIntegerField(default=1)
    state_product = models.TextField(default="no_add")
    user = models.ForeignKey(User)


class News(models.Model):
    header = models.CharField(max_length=50)
    picture = models.ImageField()
    descriptions = models.TextField()
    comments = models.TextField(null=False, blank=True)


    def __str__(self):
        return self.header
