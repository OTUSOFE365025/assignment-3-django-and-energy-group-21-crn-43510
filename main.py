############################################################################
## Django ORM Standalone Python Template
############################################################################
""" This script allows you to use Django ORM from a plain Python file
    without running the web server. Useful for testing your Product model.
"""

import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

import django
django.setup()

# import your Product model
from db.models import Product

############################################################################
## START OF APPLICATION
############################################################################

# Clear old products
Product.objects.all().delete()

# Seed sample product data (same as web app)
sample_products = [
    ("012345678905", "Banana (each)", 0.39),
    ("012345678906", "Milk 1L", 2.49),
    ("012345678907", "White Bread", 1.79),
    ("111111111111", "Apple", 0.99),
    ("222222222222", "Eggs (Dozen)", 3.49),
]

for upc, name, price in sample_products:
    Product.objects.create(upc=upc, name=name, price=price)

# Print all products to confirm
for p in Product.objects.all():
    print(f"{p.upc} → {p.name}: ${p.price}")
