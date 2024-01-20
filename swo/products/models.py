from django.db import models
'''

'''
class Product(models.Model):
    article_no = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    in_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100)
    in_stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.product
