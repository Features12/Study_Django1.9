from django.contrib.auth.models import User
from django.db import models


class Shop_List(models.Model):
    name = models.CharField(max_length=30) # имя
    kind = models.CharField(max_length=30) # вид
    price = models.FloatField() # цена
    manufacturer = models.CharField(max_length=30) # производитель
    date_receipt = models.DateField() # дата поступления
    type_form = models.TextField(default="1-object") # форма отпуска


class Shop_Cart(models.Model):
    number_product = models.ForeignKey(Shop_List)
    quantity_product = models.PositiveIntegerField(default=1)
    state_product = models.TextField(default="no_add")
    user = models.ForeignKey(User)
