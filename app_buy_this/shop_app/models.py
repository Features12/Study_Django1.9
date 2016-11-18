from django.db import models


class Shop_List(models.Model):
    name = models.CharField(max_length=30) # имя
    kind = models.CharField(max_length=30) # вид
    price = models.FloatField() # цена
    manufacturer = models.CharField(max_length=30) # производитель
    date_receipt = models.DateField(null=True) # дата поступления
    type_form = models.TextField(default="1-object") # форма отпуска


