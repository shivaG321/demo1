from django.db import models
# Create your models here.
category_choices = (
    ('Electronics', 'Electronics'),
    ('Household', 'Household'),
    ('Grocerry', 'Grocerry'),
    ('Clothing', 'Clothing'),
    ('Furniture', 'Furniture'),
    ('Books', 'Books'),
)
seller_choices = (
    ('Amazone', 'Amazone'),
    ('Flipcart', 'Flipcart'),
    ('Myntra', 'Myntra'),
    ('Ebay', 'Ebay'),
    ('Snapdeal', 'Snapdeal')
)
status_choices = (
    ('Recieved', 'Recieved'),
    ('Pending', 'Pending'),
    ('Delievered', 'Delievered')
)
payment_choices = (
    ('COD', 'COD'),
    ('Prepaid', 'Prepaid')
)

class Product(models.Model):
    pname = models.CharField(max_length=39)
    pcat = models.CharField(max_length=38, choices=category_choices)
    pqty = models.IntegerField()
    pprice = models.FloatField()
    ppayment = models.CharField(max_length=37, choices=payment_choices)
    pseller = models.CharField(max_length=43, choices=seller_choices)
    pstatus = models.CharField(max_length=42, choices=status_choices)