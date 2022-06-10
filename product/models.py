from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length =256, null=False)


class Product(models.Model):
    name = models.CharField(max_length =256, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.CharField(max_length =256, null=False)
    desc = models.CharField(max_length =256, null=False)
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)

class OrderStatus(models.Model):
    status = models.CharField(max_length =256, null=False)

class ProductOrder(models.Model):
    num = models.IntegerField(null=False)

class UserOrder(models.Model):
    address = models.CharField(max_length =256, null=False)
    time = models.DateTimeField(auto_now_add=True)
    product_price = models.IntegerField(null=False)
    discount = models.FloatField(null=False)
    total_price = models.IntegerField(null=False)
    boolean = models.CharField(max_length =256, null=False)
    num = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)





