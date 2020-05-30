from django.db import models

# For each model, always have both __str__(self) and a get_absolute_url(self) method
# Make all fields required with blank = False and for number fields, specify null = False as well
class Customer(models.Model):
    full_name = models.CharField(max_length=60, blank = False)
    email = models.CharField(max_length=100, blank = False)

    def __str__(self):
        return self.full_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=30, blank = False)
    date_purchased = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank = False, null = False)

    def __str__(self):
        return self.product_name


