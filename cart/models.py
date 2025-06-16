from django.db import models
from shopapp.models import Product


# Create your models here.


class Cart(models.Model):
    # objects = None
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)


class CartItem(models.Model):
    # DoesNotExist = None
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def Sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)
