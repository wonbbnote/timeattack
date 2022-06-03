from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20, null=False)


class Drink(models.Model):
    name = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

