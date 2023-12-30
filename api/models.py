from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    quantity = models.PositiveBigIntegerField()
    Price = models.PositiveBigIntegerField()
    discount_percentage = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    totalamount = models.PositiveBigIntegerField()