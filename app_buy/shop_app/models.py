from django.db import models

class Shop_List(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=30)
    price = models.FloatField()


    def __str__(self):
        return self.name
